import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from tkcalendar import Calendar, DateEntry
import datetime

from classes_diversas import manipular_janela
from classes_diversas import calculadora
from classes_diversas import manipular_aquivos
from repositorio import operar_tabela_bsds


rs_bsd = operar_tabela_bsds.pesquisar()

def gerar_bsd():
    try:
        if (not tree_bsd.selection()):
            raise Exception("Nenhum cadastro selecionado.")
        
        item_selecionado = tree_bsd.selection()[0]
        valores = tree_bsd.item(item_selecionado, 'values')
        #id = valores[0]
        nome = valores[1]
        cpf = valores[2]
        cargo = valores[3]
        finalidade = valores[4]
        data_inicio = valores[5]
        data_retorno = valores[6]
        municipio_origem = valores[7]
        municpio_destino = valores[8]
        valor_unitario = float(valores[9])

        data1 = datetime.datetime.strptime(data_inicio, '%Y-%m-%d')
        data2 = datetime.datetime.strptime(data_retorno, '%Y-%m-%d')
        dias = calculadora.calcular_dias(data1, data2)
        valor_total = dias * valor_unitario

        manipular_aquivos.gerar_bsd(nome, cpf, cargo, finalidade, data_inicio, data_retorno, municipio_origem, municpio_destino, dias, valor_unitario, valor_total) 
    except Exception as e:
        messagebox.showinfo("Aviso!", e)

janela_csd = tk.Tk()

janela_csd.title("Gerar Solicitação de Diária")
#manipular_janela.centralizar_janela(janela_csd)
#janela_csd.geometry("440x300")

#instancia um elemento label
label_solicitacao = tk.Label(janela_csd, text="Solicitação:")
label_solicitacao.grid(column=0, row=0, padx=5, pady=5, sticky="w")

#instancia um elemento tree
tree_bsd = ttk.Treeview(janela_csd, columns=("id", "nome", "cpf", "cargo", "finalidade", "dt_i", "dt_r", "mun_o", "mun_d", "valor_unit"), show="headings")

#define as colunas do objeto tree_bsd
tree_bsd.heading("id", text="ID")
tree_bsd.heading("nome", text="NOME")
tree_bsd.heading("cpf", text="CPF")
tree_bsd.heading("cargo", text="CARGO")
tree_bsd.heading("finalidade", text="FINALIDADE")
tree_bsd.heading("dt_i", text="DATA INÍCIO")
tree_bsd.heading("dt_r", text="DATA RETORNO")
tree_bsd.heading("mun_o", text="MINICPIO ORIGEM")
tree_bsd.heading("mun_d", text="MUNICIPIO DESTINO")
tree_bsd.heading("valor_unit", text="VALOR UNITÁRIO")

tree_bsd.column("id", width=10)
tree_bsd.column("nome", width=150)
tree_bsd.column("cpf", width=100)
tree_bsd.column("cargo", width=100)
tree_bsd.column("finalidade", width=200)
tree_bsd.column("dt_i", width=100)
tree_bsd.column("dt_r", width=100)
tree_bsd.column("mun_o", width=150)
tree_bsd.column("mun_d", width=150)
tree_bsd.column("valor_unit", width=100)

tree_bsd.grid(column=0, row=1, padx=5, pady=5)

# Popular a Listbox com dados do resultado de um SELECT da tabela bsds do banco_de_dados.db
for item in rs_bsd:
    tree_bsd.insert("", tk.END, values=(item[0], item[1], item[2], item[3], item[8], item[4], item[5], item[6], item[7], item[9]))

#instancia um objeto do tipo button
button_gerar = tk.Button(janela_csd, text="Gerar Solicitação de Diária", command=lambda: gerar_bsd())
button_gerar.grid(column=0, row=2, padx=5, pady=5, sticky="we")

janela_csd.mainloop()