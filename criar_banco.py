import sqlite3


conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")


cursor.execute("DELETE FROM produto")


produtos = [
    (1, "Dell Inspiron 15", 3500.00),
    (2, "Logitech MX Master 3S", 480.00),
    (3, "Keychron K2", 650.00),
    (4, "LG UltraGear 27GR75Q", 1899.00),
    (5, "HyperX Cloud III", 799.00),
    (6, "Razer DeathAdder V3", 549.00),
    (7, "Samsung Galaxy Book4", 4299.00),
    (8, "ASUS TUF Gaming A15", 5799.00),
    (9, "Kingston NV3 1TB", 499.00),
    (10, "WD Black SN850X 2TB", 1099.00)
]


cursor.executemany(
    "INSERT INTO produto (id, nome, preco) VALUES (?, ?, ?)",
    produtos
)


conexao.commit()
conexao.close()


print("Banco criado com sucesso.")
