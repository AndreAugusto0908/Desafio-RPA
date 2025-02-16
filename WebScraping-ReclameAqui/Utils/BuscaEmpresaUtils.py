def buscaEmpresa(navegador):
    for i in range(1, 17):
        navegador.find_element('xpath','/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div/input').click()
        navegador.find_element('xpath',f'/html/body/section[2]/div/div/div[2]/astro-island/div/div[1]/div/div[2]/ul[13]/li[{i}]/button').click()
        for j in range(1,4):
            if verificarSeContemEmpresa(navegador):
                print(f"Categoria {i} não contém empresas. Pulando...")
                break

            nomeEmpresa = navegador.find_element('xpath',f'/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/div[1]/a[{j}]/div/div/div/div[2]/div/div[1]/span').text
            notaEmpresa = navegador.find_element('xpath',f'/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/div[1]/a[{j}]/div/div/div/div[2]/div/div[2]/div/span[1]').text
            print(nomeEmpresa + " - " + notaEmpresa)

def verificarSeContemEmpresa(navegador):
    try:
        mensagem = navegador.find_element('xpath', '/html/body/section[2]/div/div/div[2]/astro-island/div/div[2]/div[1]/div/h3').text
        if mensagem == 'Não encontramos "Melhores empresas" para esta categoria':
            return True
    except:
        return False