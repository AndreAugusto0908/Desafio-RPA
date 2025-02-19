import Services.ScrapperService as ScrapperService
import Services.PlanilhaService as planilhaService

ScrapperService.abrindoPagina()
lojas = ScrapperService.pioresNotas()
planilhaService.escrevendoPlanilha(lojas)
