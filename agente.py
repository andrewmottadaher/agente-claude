import json

from anthropic import Anthropic

from ferramentas import tools, executar_ferramenta


client = Anthropic()


def enviar_mensagem(messages):

    return client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1000,
        tools=tools,
        messages=messages
    )


def processar_ferramentas(response):

    tool_results = []

    for block in response.content:

        if block.type == "tool_use":

            resultado = executar_ferramenta(
                block.name,
                block.input
            )

            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(
                        resultado,
                        ensure_ascii=False
                    )
                }
            )

    return tool_results


def executar_agente(pergunta, messages):

    messages.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    while True:

        response = enviar_mensagem(messages)

        messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

        if response.stop_reason == "end_turn":

            return response.content[0].text

        if response.stop_reason == "tool_use":

            tool_results = processar_ferramentas(response)

            messages.append(
                {
                    "role": "user",
                    "content": tool_results
                }
            )


def iniciar_conversa():

    messages = []

    print("Agente iniciado! Digite 'sair' para encerrar.")

    while True:

        pergunta = input("\nUsuário: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:

            print("\nAgente encerrado.")
            break

        resposta = executar_agente(
            pergunta,
            messages
        )

        print(f"Claude: {resposta}")


if __name__ == "__main__":

    iniciar_conversa()