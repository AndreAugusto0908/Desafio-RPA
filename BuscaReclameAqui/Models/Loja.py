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
        self.percentual_voltariam = voltariam if voltariam != "--%" else "0%"
        self.percentual_indice_solucao = indice_solucao if indice_solucao != "--%" else "0%"
        self.percentual_respondido = percentual_respondido if percentual_respondido != "--%" else "0%"
        self.numero_solicitacoes = int(numero_solicitacoes)
        
    def __repr__(self):
        return (f"Loja(nome={self.nome}, nota={self.nota}, href={self.href}, "
                f"voltariam={self.percentual_voltariam}, indice_solucao={self.percentual_indice_solucao}, "
                f"percentual_respondido={self.percentual_respondido}, "
                f"numero_solicitacoes={self.numero_solicitacoes})")
