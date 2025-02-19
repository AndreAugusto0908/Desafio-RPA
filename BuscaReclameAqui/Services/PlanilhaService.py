import pandas as pd

def escrevendoPlanilha(lojas):
        dados = [{
        "Nome": loja.nome,
        "Nota": loja.nota,
        "Link": loja.href,
        "Percentual Voltariam": loja.percentual_voltariam,
        "Índice de Solução": loja.percentual_indice_solucao,
        "Percentual Respondido": loja.percentual_respondido,
        "Número de Solicitações": loja.numero_solicitacoes
    } for loja in lojas]
        
        df = pd.DataFrame(dados)
        nome_arquivo = "lojas.xlsx"
        df.to_excel(nome_arquivo, index=False)
        return nome_arquivo