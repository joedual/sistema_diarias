import sqlite3

def inserir(nome, cpf, cargo, data_inicio, data_retorno, municipio_origem, municipio_destino, finalidade, valor_municipio):

        conn = sqlite3.connect("repositorio/banco_de_dados.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bsds (nome, cpf, cargo, data_inicio, data_retorno, municpio_origem, municipio_destino, finalidade, valor_municipio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, cargo, data_inicio, data_retorno, municipio_origem, municipio_destino, finalidade, valor_municipio))
        conn.commit()
        conn.close()

def pesquisar():
        conn = sqlite3.connect("repositorio/banco_de_dados.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM bsds")
        resultados = cursor.fetchall()
        
        conn.commit()
        conn.close()

        return resultados
