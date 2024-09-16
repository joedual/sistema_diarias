
def calcular_dias(data_inicio, data_retorno):
    diferenca = data_retorno - data_inicio
    if (diferenca.days<1):
        return -1
    else:
        return diferenca.days