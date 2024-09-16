import sqlite3

def pesquisar():
    conn = sqlite3.connect("repositorio/banco_de_dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM municipios")
    resultados = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultados