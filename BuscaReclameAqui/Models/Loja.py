import re

class Loja:
    def __init__(self, nome, nota, href):
        self.nome = nome
        self.nota = float(nota) if nota.replace('.', '', 1).isdigit() else 0.0
        self.href = href
        self.percentual_voltariam = "0%"
        self.percentual_indice_solucao = "0%"
        self.percentual_respondido = "0%"
        self.numero_solicitacoes = 0

    def formatar_dados(self, voltariam, indice_solucao, percentual_respondido, numero_solicitacoes):
        self.percentual_voltariam = re.findall(r'\d+\.?\d*%', voltariam)
        self.percentual_indice_solucao = re.findall(r'\d+\.?\d*%', indice_solucao)
        self.percentual_respondido = re.findall(r'\d+\.?\d*%', percentual_respondido)
        self.numero_solicitacoes = int(numero_solicitacoes)
        
    def __repr__(self):
        return (f"Loja(nome={self.nome}, nota={self.nota}, href={self.href}, "
                f"voltariam={self.percentual_voltariam}, indice_solucao={self.percentual_indice_solucao}, "
                f"percentual_respondido={self.percentual_respondido}, "
                f"numero_solicitacoes={self.numero_solicitacoes})")
