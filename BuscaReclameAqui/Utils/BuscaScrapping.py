import time
import re
from Models.Loja import Loja

Lojas = []

"""Percorre as categorias de moda no site, coletando o nome, a nota e o link das empresas disponíveis. 
    A função navega entre as categorias, seleciona cada empresa e armazena essas informações em uma lista de objetos Loja."""
def buscaEmpresas(navegador):
    for i in range(1, 17):
        selecionar_categoria = navegador.find_element('xpath','/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div/input')
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", selecionar_categoria)
        selecionar_categoria.click()

        selecionar_empresas = navegador.find_element('xpath',f'/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div[2]/ul[13]/li[{i}]/button')
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", selecionar_empresas)
        selecionar_empresas.click()

        time.sleep(0.2)

        empresas = navegador.find_elements('xpath','/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/div[1]/a')
        
        for j in range(len(empresas)):
            try:
                nomeEmpresa = empresas[j].find_element('xpath', './/div/div/div/div[2]/div/div[1]/span').text
                notaEmpresa = empresas[j].find_element('xpath', './/div/div/div/div[2]/div/div[2]/div/span[1]').text
                href = empresas[j].get_attribute('href')
                nova_loja = Loja(nomeEmpresa, notaEmpresa, href)
                Lojas.append(nova_loja)
            except:
                break
    return Lojas


"""Acessa a página principal da empresa no Reclame Aqui e coleta dados como número de solicitações, percentual de respostas, 
    percentual de clientes que voltariam a fazer negócio e o índice de solução. Após obter essas informações, os dados são formatados 
    e armazenados no objeto Loja antes de fechar o navegador."""
def pesquisarEmpresa(navegador, loja):
    navegador.get(loja.href)
    numero_solicitacoes = navegador.find_element('xpath', '//*[@id="newPerformanceCard"]/div[2]/div[1]/span/strong').text
    percentual_respondido = navegador.find_element('xpath', '//*[@id="newPerformanceCard"]/div[2]/div[2]/span').text
    percentual_voltariam = navegador.find_element('xpath', '//*[@id="newPerformanceCard"]/div[2]/div[5]/span/strong').text
    percentual_indice_solucao = navegador.find_element('xpath', '//*[@id="newPerformanceCard"]/div[2]/div[6]/span').text
    numero_solicitacoes = re.findall(r'\d+', numero_solicitacoes)[0]
    loja.formatar_dados(percentual_voltariam, percentual_indice_solucao, percentual_respondido, numero_solicitacoes)
    print(loja)
    navegador.close()
    return navegador