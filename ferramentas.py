from banco import buscar_produtos, analisar_produtos

ferramentas = [
    {
        "name": "buscar_produtos",
        "description": (
                "Busca registros de produtos no banco de dados usando filtros opcionais por nome e faixa de preço. Retorna os registros completos, incluindo id, nome e preço. Também permite ordenar os resultados e limitar a quantidade retornada. Use esta ferramenta quando o usuário perguntar qual produto é o mais barato ou mais caro, ou quando precisar dos dados completos de um produto."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "nome": {
                    "type": "string",
                    "description": (
                        "Parte do nome do produto que deve ser pesquisado."
                    )
                },
                "preco_minimo": {
                    "type": "number",
                    "description": "Preço mínimo da busca."
                },
                "preco_maximo": {
                    "type": "number",
                    "description": "Preço máximo da busca."
                },
                "ordenar_por": {
                    "type": "string",
                    "enum": ["id", "nome", "preco"],
                    "description": (
                        "Campo usado para ordenar os resultados."
                    )
                },
                "ordem": {
                    "type": "string",
                    "enum": ["asc", "desc"],
                    "description": (
                        "Define se os resultados serão ordenados "
                        "em ordem crescente ou decrescente."
                    )
                },
                "limite": {
                    "type": "integer",
                    "minimum": 1,
                    "description": (
                        "Quantidade máxima de produtos que deve ser retornada."
                    )
                },
                "offset": {
                    "type": "integer",
                    "minimum": 0,
                    "description": (
                        "Quantidade de resultados que devem ser ignorados antes de retornar os produtos."
                    )
                }
            },
            "required": []
        },
        "function": buscar_produtos
    },
    {
        "name": "analisar_produtos",
        "description": (
            "Realiza análises numéricas sobre os produtos do banco de dados. Pode contar produtos, calcular o preço médio, encontrar o menor preço ou encontrar o maior preço. Retorna apenas o valor numérico da análise, e não o registro completo do produto. Use esta ferramenta quando a pergunta pedir uma métrica numérica. Quando o usuário perguntar qual é o produto mais barato ou mais caro, use buscar_produtos() para obter o registro completo do produto."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "operacao": {
                    "type": "string",
                    "enum": [
                        "contagem",
                        "media",
                        "menor_preco",
                        "maior_preco"
                    ],
                    "description": (
                        "Tipo de análise que deve ser realizada."
                    )
                },
                "preco_minimo": {
                    "type": "number",
                    "description": "Preço mínimo da faixa analisada."
                },
                "preco_maximo": {
                    "type": "number",
                    "description": "Preço máximo da faixa analisada."
                }
            },
            "required": ["operacao"]
        },
        "function": analisar_produtos
    }
]

tools = [
    {
        "name": ferramenta["name"],
        "description": ferramenta["description"],
        "input_schema": ferramenta["input_schema"]
    }
    for ferramenta in ferramentas
]

def executar_ferramenta(nome, entrada):

    for ferramenta in ferramentas:

        if ferramenta["name"] == nome:

            funcao = ferramenta["function"]

            try:
                return funcao(**entrada)

            except Exception as erro:
                return (
                    f"Erro ao executar a ferramenta "
                    f"'{nome}': {erro}"
                )

    return f"Ferramenta desconhecida: {nome}"