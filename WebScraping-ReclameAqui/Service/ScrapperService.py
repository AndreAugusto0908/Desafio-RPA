import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import Utils.BuscaEmpresaUtils as BuscaEmpresaUtils

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)
paginaDeBusca = 'https://www.reclameaqui.com.br/'


def abrindoPagina():
    navegador.get(paginaDeBusca)
    time.sleep(3)
    navegador.find_element('xpath', '//*[@id="adopt-accept-all-button"]').click()
def melhoresNotas():
    BuscaEmpresaUtils.buscaEmpresa(navegador)

def pioresNotas():
    navegador.find_element('xpath', '/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/ul/li[2]').click()
    BuscaEmpresaUtils.buscaEmpresa(navegador)

