import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from tkcalendar import Calendar, DateEntry
from datetime import datetime

from classes_diversas import manipular_janela
from repositorio import operar_tabela_municipios
from repositorio import operar_tabela_funcionarios
from repositorio import operar_tabela_bsds

funcionarios = operar_tabela_funcionarios.pesquisar()

rs_municipios = operar_tabela_municipios.pesquisar()

def cadastrar():
    try:
        combo_box_texto = combo_box_funcionario.get()
        funcionario = combo_box_texto.split(" / ")
        
        nome = funcionario[0]
        cpf = funcionario[1]
        cargo = funcionario[2]
        data_inicio = calendario_input_data_inicio.get_date()
        data_retorno = calendario_input_data_retorno.get_date()
        
        if data_inicio == data_retorno:
            raise Exception("As datas são iguais.")
        elif  data_inicio > data_retorno:
            raise Exception("A data inicial é posterior à data final.")

        municipio_origem = combo_box_cidade_origem.get()
        municipio_d = combo_box_cidade_destino.get().split(" / ")
        municipio_destino = municipio_d[0]
        valor_destino = float(municipio_d[1])

        if municipio_origem == municipio_destino:
            raise Exception("Os municípios devem ser diferentes")
        
        finalidade = text_finalidade.get(1.0, tk.END)
        
        operar_tabela_bsds.inserir(nome, cpf, cargo, data_inicio, data_retorno, municipio_origem, municipio_destino, finalidade, valor_destino)
        tk.messagebox.showinfo("Aviso!", "Cadastro realizado com sucesso.")
        
    except Exception as e:
        messagebox.showinfo("Aviso!", e)

janela_csd = tk.Tk()

janela_csd.title("Cadastrar Diária")
manipular_janela.centralizar_janela(janela_csd)
janela_csd.geometry("360x300")

#instancia um elemento label
label_funcionario = tk.Label(janela_csd, text="Funcionário:", width=10)
label_funcionario.grid(column=0, row=0, padx=5, pady=5, sticky="w")

#instancia um elemento combo_box
combo_box_funcionario = ttk.Combobox(janela_csd, state="readonly", width=38)
combo_box_funcionario.grid(column=1, row=0, padx=5, pady=5, sticky="ew")
combo_box_funcionario['values']= [(item[1]+" / "+item[2]+" / "+item[3]) for item in funcionarios] #preenche o combobox com NOMES E CPFS resultado de um SELECT da tabela funcionarios do banco_de_dados.db
combo_box_funcionario.current(0)  # define o item selecionado


label_data_inicio = tk.Label(janela_csd, text="Data Início:")
label_data_inicio.grid(column=0, row=1, padx=5, pady=5, sticky="w")

calendario_input_data_inicio = DateEntry(janela_csd, bd=2)
calendario_input_data_inicio.grid(column=1, row=1, sticky="ew", padx=5, pady=5)

label_data_retorno = tk.Label(janela_csd, text="Data Retorno:")
label_data_retorno.grid(column=0, row=2, padx=5, pady=5, sticky="w")

calendario_input_data_retorno = DateEntry(janela_csd, bd=2)
calendario_input_data_retorno.grid(column=1, row=2, sticky="ew", padx=5, pady=5)

label_cidade_origem = tk.Label(janela_csd, text="Cidade Origem:")
label_cidade_origem.grid(column=0, row=3, padx=5, pady=5, sticky="w")

combo_box_cidade_origem = ttk.Combobox(janela_csd, state="readonly")
combo_box_cidade_origem.grid(column=1, row=3, columnspan=2, sticky="ew", padx=5, pady=5)
combo_box_cidade_origem['values']= [(item[1]) for item in rs_municipios]
combo_box_cidade_origem.current(0)  # define o item selecionado


label_cidade_destino = tk.Label(janela_csd, text="Cidade Destino:")
label_cidade_destino.grid(column=0, row=4, padx=5, pady=5, sticky="w")

combo_box_cidade_destino = ttk.Combobox(janela_csd, state="readonly")
combo_box_cidade_destino.grid(column=1, row=4, columnspan=2, sticky="ew", padx=5, pady=5)
combo_box_cidade_destino['values'] = [(item[1]+" / "+str(item[2])) for item in rs_municipios]
combo_box_cidade_destino.current(1)  # define o item selecionado

label_finalidade = tk.Label(janela_csd, text="Cidade Destino:")
label_finalidade.grid(column=0, row=5, padx=5, pady=5, columnspan=2, sticky="w")

text_finalidade = tk.Text(janela_csd, height=2, width=2)
text_finalidade.grid(column=0, row=6, columnspan=2, sticky="ew", padx=5, pady=5)

botao = tk.Button(janela_csd, text="Salvar", command=lambda:cadastrar())
botao.grid(column=0, row=7, padx=5, pady=5, columnspan=2, sticky="ew")

janela_csd.mainloop()