"""Retorna o valor percentual informado ou 'não informado' caso esteja vazio."""
def tratar_percentual(valor):
    return valor if valor != "" else "não informado"