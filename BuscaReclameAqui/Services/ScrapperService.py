import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import Utils.BuscaScrapping as BuscaScrapping
import Utils.FormatandoString as FormatandoString


servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)
paginaDeBusca = 'https://www.reclameaqui.com.br/'
Lojas = []

def abrindoPagina():
    navegador.get(paginaDeBusca)
    navegador.fullscreen_window()
    navegador.find_element('xpath', '//*[@id="adopt-accept-all-button"]').click()
    lista_de_categorias = navegador.find_element('xpath','/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]')
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", lista_de_categorias)
    time.sleep(3)

def melhoresNotas():
    Lojas = BuscaScrapping.buscaEmpresas(navegador)
    top_3_lojas = sorted(Lojas, key=lambda x: float(x.nota.replace(',', '.')), reverse=True)[:3]
    print(top_3_lojas)
    for loja in top_3_lojas:
        url = FormatandoString.formatarParaLink(str(loja.nome))
        navegador.quit()
        navegador2 = webdriver.Firefox(service=servico)
        BuscaScrapping.pesquisarEmpresa(url, navegador2, loja)


def pioresNotas():
    navegador.find_element('xpath', '/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/ul/li[2]').click()
    BuscaScrapping.buscaEmpresas(navegador)

