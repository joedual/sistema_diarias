import tkinter as tk
import subprocess
from classes_diversas import manipular_janela

def abrir_cad_funcionario(janela):
    #oculta a janela
    janela.withdraw()
    #executa o subprocesso cadastrar_funcionario.py
    subprocess.call(["python", "gui_cadastrar_funcionario.py"])
    janela.deiconify()

def abrir_cad_sol_diaria(janela):
    janela.withdraw()
    subprocess.call(["python", "gui_cadastrar_sol_diaria.py"])
    janela.deiconify()

def abrir_gerar_sol_diaria(janela):
    janela.withdraw()
    subprocess.call(["python", "gui_gerar_sol_diaria.py"])
    janela.deiconify()


#instancia um objeto do tipo tkinter
janela_principal = tk.Tk()
janela_principal.title("Sistema de Controle de Diárias")
manipular_janela.centralizar_janela(janela_principal)
janela_principal.columnconfigure(0, weight=1)

#instancia objetos do tipo button
button_cad_funcionario = tk.Button(janela_principal, text="Cadastrar Funcionário", command=lambda:abrir_cad_funcionario(janela_principal))
button_cad_funcionario.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

button_cad_sol_diaria = tk.Button(janela_principal, text="Cadastrar Diária", command=lambda:abrir_cad_sol_diaria(janela_principal))
button_cad_sol_diaria.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

button_gerar_sol_diaria = tk.Button(janela_principal, text="Gerar Solicitação de Diária", command=lambda:abrir_gerar_sol_diaria(janela_principal))
button_gerar_sol_diaria.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")

janela_principal.mainloop()
