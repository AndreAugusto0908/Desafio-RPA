def buscaEmpresa(navegador):
    for i in range(1, 17):
        navegador.find_element('xpath','/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div/input').click()
        navegador.find_element('xpath',f'/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div[2]/ul[13]/li[{i}]/button').click()

        empresas = navegador.find_elements('xpath',
                                               '/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/div[1]/a')
        for j in range(len(empresas)):
            try:
                nomeEmpresa = empresas[j].find_element('xpath', './/div/div/div/div[2]/div/div[1]/span').text
                notaEmpresa = empresas[j].find_element('xpath', './/div/div/div/div[2]/div/div[2]/div/span[1]').text
                print(nomeEmpresa + " - " + notaEmpresa)
            except:
                break

def verificarSeContemEmpresa(navegador):
    try:
        mensagem = navegador.find_element('xpath', '/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/div[1]/div/h3').text
        if mensagem == 'Não encontramos "Melhores empresas" para esta categoria':
            return True
    except:
        return False
