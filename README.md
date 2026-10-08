\# Agente de IA com Python e Claude



Projeto de estudo desenvolvido em Python para compreender, na prática, o funcionamento de um agente de IA utilizando a API da Anthropic (Claude). Este projeto explora conceitos como integração com LLMs, tool use, seleção e execução de ferramentas, manutenção do contexto da conversa e integração com banco de dados.



\## Objetivo



O objetivo principal é entender como diferentes componentes de um agente de IA se relacionam:



Usuário -> Agente em Python -> Claude -> Seleção de ferramenta -> Execução em Python -> Banco de dados SQLite -> Resultado -> Claude -> Resposta ao usuário



\## Funcionalidades atuais



O agente atualmente possui:



integração com a API do Claude;

ferramentas próprias desenvolvidas em Python;

seleção de ferramentas pelo modelo;

execução de múltiplas ferramentas em uma mesma interação;

manutenção do contexto da conversa;

integração com banco de dados SQLite;

consultas SQL parametrizadas;

filtros por nome e faixa de preço;

ordenação;

limite e paginação;

consultas para obtenção de registros completos;

operações de análise numérica.



\# As ferramentas disponíveis atualmente são:



buscar\_produtos

analisar\_produtos



\## Estrutura do projeto:



agente-claude/

├── agente.py

├── banco.py

├── criar\_banco.py

├── ferramentas.py

├── requirements.txt

├── README.md

└── .gitignore



agente.py

Responsável pela comunicação com o Claude, manutenção do histórico da conversa e processamento das solicitações de ferramentas.



banco.py

Contém a lógica de acesso ao banco de dados SQLite e as operações de consulta e análise dos produtos.



criar\_banco.py

Cria e popula o banco de dados utilizado pelo projeto.



ferramentas.py

Define as ferramentas que podem ser utilizadas pelo modelo e faz a ligação entre as solicitações do Claude e as funções Python responsáveis pela execução.



\## Tecnologias: Python, Anthropic API, Claude Haiku 4.5, SQLite, SQL, Git.



\## Como executar



1\. Criar o ambiente virtual.

No Windows PowerShell: python -m venv .venv



2\. Ativar o ambiente virtual

No Windows PowerShell: .venv\\Scripts\\Activate.ps1



3\. Instalar as dependências

No Windows PowerShell: pip install -r requirements.txt



4\. Configurar a chave da API

Defina a variável de ambiente: ANTHROPIC\_API\_KEY



5\. Criar o banco de dados

No Windows PowerShell: python criar\_banco.py



6\. Executar o agente

No Windows PowerShell: python agente.py



O usuário pode fazer perguntas como:



\## Exemplo



O usuário pode fazer perguntas como:



Quais são os dois produtos mais baratos?



ou



Qual é o preço médio dos produtos entre 500 e 2000 reais?



O Claude identifica quais ferramentas são necessárias, a aplicação executa as operações correspondentes e os resultados são utilizados para elaborar a resposta.



\## Segurança



O projeto utiliza ferramentas com parâmetros estruturados em vez de permitir que o modelo execute SQL arbitrário diretamente.



As consultas ao banco utilizam parâmetros SQL para os valores fornecidos pelo usuário.



A validação das entradas é realizada pela aplicação Python, e não apenas pelo modelo de linguagem.



\## Status



Projeto em desenvolvimento e utilizado como parte dos meus estudos sobre desenvolvimento de agentes de IA, Python, APIs e integração com bancos de dados.



Novas funcionalidades e melhorias de validação, segurança e arquitetura serão adicionadas conforme o projeto evoluir.



\## Uso de ferramentas de IA



Este projeto faz parte do meu processo de aprendizagem. Durante o desenvolvimento, utilizo ferramentas de IA como apoio para compreender conceitos, discutir implementações, revisar código e identificar possíveis melhorias. A implementação é utilizada como parte do processo de estudo e compreensão dos conceitos envolvidos.

