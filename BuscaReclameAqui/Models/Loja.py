import re

"""Representa uma loja com informações coletadas do Reclame Aqui, incluindo nome, nota, link, 
    percentual de clientes que voltariam a fazer negócio, índice de solução, percentual de respostas 
    e número total de solicitações."""
class Loja:
    def __init__(self, nome, nota, href):
        self.nome = nome
        self.nota = float(nota) if nota.replace('.', '', 1).isdigit() else 0.0
        self.href = href
        self.percentual_voltariam = "0%"
        self.percentual_indice_solucao = "0%"
        self.percentual_respondido = "0%"
        self.numero_solicitacoes = 0

    """Formata e armazena os dados coletados sobre a empresa, extraindo os percentuais e convertendo 
        o número de solicitações para inteiro."""
    def formatar_dados(self, voltariam, indice_solucao, percentual_respondido, numero_solicitacoes):
        self.percentual_voltariam = re.findall(r'\d+\.?\d*%', voltariam)
        self.percentual_voltariam = self.percentual_voltariam[0] if self.percentual_voltariam else ""
        self.percentual_indice_solucao = re.findall(r'\d+\.?\d*%', indice_solucao)
        self.percentual_indice_solucao = self.percentual_indice_solucao[0] if self.percentual_indice_solucao else ""
        self.percentual_respondido = re.findall(r'\d+\.?\d*%', percentual_respondido)
        self.percentual_respondido = self.percentual_respondido[0] if self.percentual_respondido else ""
        self.numero_solicitacoes = int(numero_solicitacoes)
        
    def __repr__(self):
        return (f"Loja(nome={self.nome}, nota={self.nota}, href={self.href}, "
                f"voltariam={self.percentual_voltariam}, indice_solucao={self.percentual_indice_solucao}, "
                f"percentual_respondido={self.percentual_respondido}, "
                f"numero_solicitacoes={self.numero_solicitacoes})")
