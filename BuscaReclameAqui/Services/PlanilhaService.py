import pandas as pd

def tratar_percentual(valor):
    return valor if valor != "" else "não informado"

def escrevendoPlanilha(lojas):
    dados = [{
        "Nome": loja.nome,
        "Nota": loja.nota,
        "Link": loja.href,
        "Percentual Voltariam": tratar_percentual(loja.percentual_voltariam),
        "Índice de Solução": tratar_percentual(loja.percentual_indice_solucao),
        "Percentual Respondido": tratar_percentual(loja.percentual_respondido),
        "Número de Solicitações": loja.numero_solicitacoes
    } for loja in lojas]
    
    df = pd.DataFrame(dados)
    nome_arquivo = "lojas.xlsx"
    df.to_excel(nome_arquivo, index=False)
    return nome_arquivo
    