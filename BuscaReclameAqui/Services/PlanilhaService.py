import pandas as pd
import Utils.FormatarString as formatarString
from datetime import datetime

"""Gera uma planilha Excel com os dados das lojas, incluindo nome, nota, link, percentual de clientes que voltariam, 
    índice de solução, percentual de respostas e número de solicitações. O arquivo é salvo com um nome contendo a data e hora da execução."""
def escrevendoPlanilha(lojas):
    dados = [{
        "Nome": loja.nome,
        "Nota": loja.nota,
        "Link": loja.href,
        "Percentual Voltariam": formatarString.tratar_percentual(loja.percentual_voltariam),
        "Índice de Solução": formatarString.tratar_percentual(loja.percentual_indice_solucao),
        "Percentual Respondido": formatarString.tratar_percentual(loja.percentual_respondido),
        "Número de Solicitações": loja.numero_solicitacoes
    } for loja in lojas]
    
    df = pd.DataFrame(dados)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nome_arquivo = f"Lista_Loja_{timestamp}.xlsx"
    
    df.to_excel(nome_arquivo, index=False)
    return nome_arquivo
    