import Services.ScrapperService as ScrapperService
import Services.PlanilhaService as planilhaService

ScrapperService.abrindoPagina()
lojas = ScrapperService.melhoresNotas()
piores_lojas = ScrapperService.pioresNotas()

todas_lojas = lojas + piores_lojas
planilhaService.escrevendoPlanilha(todas_lojas)
