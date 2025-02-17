from Models.Loja import Loja

Lojas = []
def buscaEmpresas(navegador):
    for i in range(1, 17):
        navegador.find_element('xpath', '/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div/input').click()
        navegador.find_element('xpath',f'/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div[2]/ul[13]/li[{i}]/button').click()

        empresas = navegador.find_elements('xpath','/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/div[1]/a')
        for j in range(len(empresas)):
            try:
                nomeEmpresa = empresas[j].find_element('xpath', './/div/div/div/div[2]/div/div[1]/span').text
                notaEmpresa = empresas[j].find_element('xpath', './/div/div/div/div[2]/div/div[2]/div/span[1]').text
                nova_loja = Loja(nomeEmpresa, notaEmpresa)
                Lojas.append(nova_loja)
            except:
                break
    return Lojas

def pesquisarEmpresa(url, navegador, loja):
    navegador.get(url)
    percentual_respondido = navegador.find_element('xpath', '//*[@id="newPerformanceCard"]/div[2]/div[2]/span').text
    voltariam = navegador.find_element('xpath', '//*[@id="newPerformanceCard"]/div[2]/div[5]/span/strong').text
    indice_solucao = navegador.find_element('xpath', '//*[@id="newPerformanceCard"]/div[2]/div[6]/span').text
    loja.voltariam = voltariam
    loja.indice_solucao = indice_solucao
    loja.percentual_respondido = percentual_respondido
    print(loja.nome)
    print(loja.nota)
    print(loja.voltariam)
    print(loja.indice_solucao)
    print(loja.percentual_respondido)
    return navegador