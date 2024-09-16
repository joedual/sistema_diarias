import tkinter as tk
from classes_diversas import manipular_janela
from repositorio import operar_tabela_funcionarios

def cadastrar():
    try:
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        cargo = entry_cargo.get()
        if not nome or not cpf or not cargo:
            raise Exception("O preenchimento dos campos são necessários.")

        operar_tabela_funcionarios.inserir(nome, cpf, cargo)
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)
        tk.messagebox.showinfo("Aviso!", "Cadastro realizado com sucesso.")
    except Exception as e:
        tk.messagebox.showinfo("Aviso!", e)


janela_cf = tk.Tk()

janela_cf.title("Cadastrar Funcionário")
manipular_janela.centralizar_janela(janela_cf)
janela_cf.geometry("280x300")

label_nome = tk.Label(janela_cf, text="Nome:", width=10)
label_nome.grid(column=0, row=0, padx=5, pady=5, sticky="w")

entry_nome = tk.Entry(width=30)
entry_nome.grid(column=1, row=0, padx=5, pady=5)


label_cpf = tk.Label(janela_cf, text="CPF:", width=10)
label_cpf.grid(column=0, row=1, padx=5, pady=5, sticky="w")

entry_cpf = tk.Entry(width=30)
entry_cpf.grid(column=1, row=1, padx=5, pady=5)


label_cargo = tk.Label(janela_cf, text="Cargo:", width=10)
label_cargo.grid(column=0, row=2, padx=5, pady=5, sticky="w")

entry_cargo = tk.Entry(width=30)
entry_cargo.grid(column=1, row=2, padx=5, pady=5)

botao = tk.Button(janela_cf, text="Salvar", command=lambda:cadastrar())
botao.grid(column=0, row=5, padx=5, pady=5, columnspan=2, sticky="nsew")

janela_cf.mainloop()