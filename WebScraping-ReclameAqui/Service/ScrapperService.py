import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from Utils.BuscaEmpresaUtils import buscaEmpresa


servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)
def extraindoDados():
    navegador.get('https://www.reclameaqui.com.br/')
    time.sleep(10)
    navegador.find_element('xpath', '//*[@id="adopt-accept-all-button"]').click()
    buscaEmpresa(navegador)


extraindoDados()

