import Services.ScrapperService as ScrapperService
import Services.PlanilhaService as planilhaService


"""Executa o fluxo principal do programa, abrindo a página do Reclame Aqui, coletando as melhores e piores lojas, 
e salvando os dados em uma planilha."""

ScrapperService.abrindoPagina()
lojas = ScrapperService.melhoresNotas()
piores_lojas = []
todas_lojas = lojas + piores_lojas
planilhaService.escrevendoPlanilha(todas_lojas)
