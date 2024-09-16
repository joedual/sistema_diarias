import webbrowser

#recebe um argumento nome do arquivo e retorna uma lista com os nomes encontrados
def ler_nomes_do_arquivo(nome_arquivo):
    nomes = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            nome = linha.strip()  # Remove espaços em branco no início e no final da linha
            nomes.append(nome)
    return nomes

#gera um arquivo html com o documento preenchido com os dados do funcionário e 
def gerar_bsd(
        nome, cpf, cargo, finalidade, data_inicio,  data_retorno, municipio_origem, municpio_destino, dias, valor_unitario, valor_total):
    html_string = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Solicitação de Diárias</title>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
            </style>
        </head>
        <body>
            <h1>Solicitação de Diárias</h1>
            <table border>
                <tr>
                    <td>
                        Nome:
                    </td>
                    <td colspan='3'>
                        """+nome+"""
                    </td>
                </tr>

                <tr>
                    <td>
                       Data Incicio:
                    </td>
                    <td>
                        """+data_inicio+"""
                    </td>
                    <td>
                       Data Retorno:
                    </td>
                    <td>
                        """+data_retorno+"""
                    </td>
                </tr>

                <tr>
                    <td>
                       Quantidade Diárias:
                    </td>
                    <td>
                        """+str(dias)+"""
                    </td>
                    <td>
                       Valor Diárias:
                    </td>
                    <td>
                        """+str(valor_unitario)+"""
                    </td>
                </tr>

                <tr>
                    <td colspan='4'>
                        Eu """+nome+""" solicito o pagamento de """+str(dias)+""" diárias, totalizando o valor de R$ """+str(valor_total)+""" referente à viagem para """+municpio_destino+""" no período de """+data_inicio+""" até """+data_retorno+""".
                    </td>
                </tr>

                <tr>
                    <td colspan='2' align=center>
                       </br>_______________________________</br>(assinatura do solicitante)
                    </td>
                    <td colspan='2' align=center>
                       </br>_______________________________</br>(assinatura da chefia imediata)
                    </td>
                </tr>
        </body>
        </html>
        """
    print ("debug")
    
    with open("index.html", "w") as f:
        f.write(html_string)

    # Abre o arquivo no navegador padrão
    webbrowser.open_new_tab("index.html")