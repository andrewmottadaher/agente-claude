import sqlite3

def conectar():
    return sqlite3.connect("loja.db")

def converter_produtos(linhas):
    return [
        {
            "id": produto[0],
            "nome": produto[1],
            "preco": produto[2]
        }
        for produto in linhas
    ]

def buscar_produtos(
    nome=None,
    preco_minimo=None,
    preco_maximo=None,
    ordenar_por="nome",
    ordem="asc",
    limite=None,
    offset=0
):
    if preco_minimo is not None and preco_minimo < 0:
        return "Erro: o preço mínimo não pode ser negativo."

    if preco_maximo is not None and preco_maximo < 0:
        return "Erro: o preço máximo não pode ser negativo."

    if (
        preco_minimo is not None
        and preco_maximo is not None
        and preco_minimo > preco_maximo
    ):
        return "Erro: o preço mínimo não pode ser maior que o preço máximo."

    if limite is not None:
        if not isinstance(limite, int) or limite <= 0:
            return "Erro: o limite deve ser um número inteiro positivo."

    colunas_permitidas = {
        "id": "id",
        "nome": "nome",
        "preco": "preco"
    }

    ordens_permitidas = {
        "asc": "ASC",
        "desc": "DESC"
    }

    if not isinstance(offset, int) or offset < 0:
        return "Erro: o offset deve ser um número inteiro não negativo."

    if ordenar_por not in colunas_permitidas:
        return "Erro: campo de ordenação inválido."

    if ordem not in ordens_permitidas:
        return "Erro: ordem de classificação inválida."

    sql = """
        SELECT id, nome, preco
        FROM produto
    """

    condicoes = []
    parametros = []

    if nome:
        condicoes.append("nome LIKE ? COLLATE NOCASE")
        parametros.append(f"%{nome}%")

    if preco_minimo is not None:
        condicoes.append("preco >= ?")
        parametros.append(preco_minimo)

    if preco_maximo is not None:
        condicoes.append("preco <= ?")
        parametros.append(preco_maximo)

    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)

    sql += (
        f" ORDER BY "
        f"{colunas_permitidas[ordenar_por]} "
        f"{ordens_permitidas[ordem]}"
    )

    if limite is not None:
        sql += " LIMIT ?"
        parametros.append(limite)

        if offset > 0:
            sql += " OFFSET ?"
            parametros.append(offset)

    elif offset > 0:
        sql += " LIMIT -1 OFFSET ?"
        parametros.append(offset)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(sql, parametros)

    produtos = cursor.fetchall()

    conexao.close()

    if not produtos:
        return "Nenhum produto encontrado."

    return converter_produtos(produtos)

def analisar_produtos(
    operacao,
    preco_minimo=None,
    preco_maximo=None
):
    operacoes_permitidas = {
        "contagem": "COUNT(*)",
        "media": "AVG(preco)",
        "menor_preco": "MIN(preco)",
        "maior_preco": "MAX(preco)"
    }

    if operacao not in operacoes_permitidas:
        return "Erro: operação de análise inválida."

    if preco_minimo is not None and preco_minimo < 0:
        return "Erro: o preço mínimo não pode ser negativo."

    if preco_maximo is not None and preco_maximo < 0:
        return "Erro: o preço máximo não pode ser negativo."

    if (
        preco_minimo is not None
        and preco_maximo is not None
        and preco_minimo > preco_maximo
    ):
        return "Erro: o preço mínimo não pode ser maior que o preço máximo."

    sql = f"""
        SELECT {operacoes_permitidas[operacao]}
        FROM produto
    """

    condicoes = []
    parametros = []

    if preco_minimo is not None:
        condicoes.append("preco >= ?")
        parametros.append(preco_minimo)

    if preco_maximo is not None:
        condicoes.append("preco <= ?")
        parametros.append(preco_maximo)

    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(sql, parametros)

    resultado = cursor.fetchone()[0]

    conexao.close()

    if resultado is None:
        return "Nenhum produto encontrado."

    return resultado