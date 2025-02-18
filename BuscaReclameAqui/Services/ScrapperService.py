import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import Utils.BuscaScrapping as BuscaScrapping
import Utils.FormatandoString as FormatandoString


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
paginaDeBusca = 'https://www.reclameaqui.com.br/'
Melhores_lojas = []
Piores_lojas = []

def abrindoPagina():
    navegador.get(paginaDeBusca)
    navegador.maximize_window()
    navegador.find_element('xpath', '//*[@id="adopt-accept-all-button"]').click()

def melhoresNotas():
    Lojas = BuscaScrapping.buscaEmpresas(navegador)
    top_3_lojas = sorted(Lojas, key=lambda x: float(x.nota.replace(',', '.')), reverse=True)[:3]
    print(top_3_lojas)
    for loja in top_3_lojas:
        url = FormatandoString.formatarParaLink(str(loja.nome))
        navegador.quit()
        navegador2 = webdriver.Chrome(service=servico)
        BuscaScrapping.pesquisarEmpresa(url, navegador2, loja)


def pioresNotas():
    navegador.find_element('xpath', '/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/ul/li[2]').click()
    Piores_lojas = BuscaScrapping.buscaEmpresas(navegador)
    lojas_nota_0 = [loja for loja in Piores_lojas if loja.nota == 0 or str(loja.nota).strip() == "0"]
    print(lojas_nota_0)
    for loja in lojas_nota_0:
        url = FormatandoString.formatarParaLink(str(loja.nome))
        navegador.quit()
        navegador2 = webdriver.Chrome(service=servico)
        BuscaScrapping.pesquisarEmpresa(url, navegador2, loja)

