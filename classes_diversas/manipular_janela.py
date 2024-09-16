def centralizar_janela(janela):
    """Centraliza uma janela na tela.
    Args:
        janela: A janela Tkinter a ser centralizada.
    """

    # Obtém as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Obtém as dimensões da janela
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()

    # Calcula as coordenadas x e y para centralizar
    x = (largura_tela / 2) - (largura_janela / 2)
    y = (altura_tela / 2) - (altura_janela / 2)

    # Posiciona a janela
    janela.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, int(x), int(y)))
