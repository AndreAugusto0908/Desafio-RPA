from unidecode import unidecode

def formatarParaLink(texto):
    if texto == 'Joias Beout':
        texto = 'Beout Joias'

    nome_sem_acentos = unidecode(texto)
    nome_formatado = nome_sem_acentos.replace(' ', '-').lower()
    url = f'https://www.reclameaqui.com.br/empresa/{nome_formatado}/'
    return url