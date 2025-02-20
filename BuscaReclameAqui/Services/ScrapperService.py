from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import Utils.BuscaScrapping as BuscaScrapping


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
paginaDeBusca = 'https://www.reclameaqui.com.br/'
Melhores_lojas = []
Piores_lojas = []

"""Abre a página inicial do Reclame Aqui, maximiza a janela e aceita os cookies e permissões necessárias para navegação."""
def abrindoPagina():
    navegador.get(paginaDeBusca)
    navegador.maximize_window()
    navegador.find_element('xpath', '//*[@id="adopt-accept-all-button"]').click()

"""Busca todas as empresas na categoria de moda, ordena por nota e retorna as três melhores. 
    Para cada uma das três melhores empresas, acessa sua página no Reclame Aqui para coletar dados detalhados."""
def melhoresNotas():
    Lojas = BuscaScrapping.buscaEmpresas(navegador)
    top_3_lojas = sorted(Lojas, key=lambda x: x.nota, reverse=True)[:3]
    for loja in top_3_lojas:
        navegador2 = webdriver.Chrome(service=servico)
        BuscaScrapping.pesquisarEmpresa(navegador2, loja)
    navegador.get(paginaDeBusca)
    return top_3_lojas


"""Busca as empresas com nota 0, ordena pelo número de solicitações e retorna as três maiores solicitações. 
    Para cada empresa de nota 0, acessa sua página no Reclame Aqui para coletar informações detalhadas."""
def pioresNotas():
    navegador.get(paginaDeBusca)
    navegador.find_element('xpath', '/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/ul/li[2]').click()
    Piores_lojas = BuscaScrapping.buscaEmpresas(navegador)
    lojas_nota_0 = [loja for loja in Piores_lojas if loja.nota == 0 or str(loja.nota).strip() == "0"]
    
    for loja in lojas_nota_0:
        navegador.quit()
        navegador2 = webdriver.Chrome(service=servico)
        BuscaScrapping.pesquisarEmpresa(navegador2, loja)
    
    lojas_nota_0.sort(key=lambda x: x.numero_solicitacoes, reverse=True)
    top_3_piores_lojas = lojas_nota_0[:3]
    return top_3_piores_lojas

