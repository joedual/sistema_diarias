import sqlite3

def inserir(nome, cpf, cargo):
    conn = sqlite3.connect("repositorio/banco_de_dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM funcionarios WHERE cpf = ?", (cpf,))
    count = cursor.fetchone()[0]
    if(count>0):
        raise Exception("Já existe um cadastro para esse CPF")
    else:
        cursor.execute("INSERT INTO funcionarios  (nome, cpf, cargo) VALUES (?, ?, ?)", (nome, cpf, cargo))
    conn.commit()
    conn.close()

def pesquisar():
    conn = sqlite3.connect("repositorio/banco_de_dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    resultados = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultados