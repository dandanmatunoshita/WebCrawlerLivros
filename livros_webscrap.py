import csv
from requests import *
from bs4 import BeautifulSoup

def trocar_caracter(nome):

    acentos = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'ç': 'c', ',': '', '"': '', "'": "",'Á': 'a', 'À': 'a', 'Â': 'a', 'Ã': 'a', 'É': 'e', 'È': 'e', 'Ê': 'e', 'Í': 'i', 'Ì': 'i', 'Î': 'i', 'Ò': 'o', 'Ó': 'o', 'Ô': 'o', 'Õ': 'o', 'Ù': 'u', 'Ú': 'u', 'Û': 'u', 'Ç': 'c'}
    texto_sem_acentos = ''

    for caracter in nome:
        if caracter.lower() in acentos:
            texto_sem_acentos += acentos[caracter]

        else:
            texto_sem_acentos += caracter

    nome = texto_sem_acentos

    return nome

#input do nome do livro
nome_do_livro = input('Nome do livro: ')
nome_do_livro.lower()
lista_nome_do_livro = nome_do_livro.split(' ')
ler = len(lista_nome_do_livro)

url_porcentagem = ''
url_mais = ''

#Transformação do nome do livro nos padrões da url
for index in lista_nome_do_livro:
    if index == lista_nome_do_livro[ler - 1]:
        url_porcentagem += index
    else:
        url_porcentagem += index + '%20'

for index in lista_nome_do_livro:
    if index == lista_nome_do_livro[ler - 1]:
        url_mais += index
    else:
        url_mais += index + '+'

#URL

url = {
    'estante_virtual' :  f'https://www.estantevirtual.com.br/busca?q={url_porcentagem}',

    'livraria_cultura' : f'https://www3.livrariacultura.com.br/busca/?ft={url_porcentagem}&originalText={url_porcentagem}',

    'livraria_leitura' : f'https://leitura.com.br/index.php?route=product/search&search={url_porcentagem}',

    'livraria_da_vila' : f'https://www.livrariadavila.com.br/{url_porcentagem}'
}


'''ESTANTE VIRTUAL'''

pagina_estante_virtual = get(url['estante_virtual'])

sopa_estante_virtual = BeautifulSoup(pagina_estante_virtual.content, 'html.parser')

#TESTAR ERRO

try:
    nome_estante_virtual = sopa_estante_virtual.find('h2', {'itemprop' : 'name'}).get_text()

    preço_estante_virtual = sopa_estante_virtual.find('span', {'class': 'preco'}).get_text()

    link_estante_virtual = sopa_estante_virtual.find('div', {'class': 'ver-livros'})

    carrinho_estante_virtual = link_estante_virtual.find('a')

    if nome_do_livro.lower() in trocar_caracter(nome_estante_virtual.lower()):

        print('__________________________________________________________________________')

        print(f'\n___ESTANTE VIRTUAL___ \n')

        print(f'--nome-- \n{nome_estante_virtual.strip()} \n \n--preço-- \n{preço_estante_virtual.strip()} \n')

        print('url:', 'www.estantevirtual.com.br' + carrinho_estante_virtual.get('href'))

    else: 
        i=1
        # print('__________________________________________________________________________')

        # print(f'\n___ESTANTE VIRTUAL___ \n')

        # print('--NÃO ENCONTRADO--')

        while nome_do_livro.lower() not in trocar_caracter(nome_estante_virtual.lower()):
            i+=1
            nomes_estante_virtual = sopa_estante_virtual.find_all('h2')

            nome_estante_virtual_2 = nomes_estante_virtual[i]

            nome_estante_virtual = nome_estante_virtual_2.get_text()

            #verificação(text_nome_estante_virtual_2)

            preço_estante_virtual = sopa_estante_virtual.find_all('span', {'class' : 'preco'})

            preço_estante_virtual_2 = preço_estante_virtual[i]

            preço_estante_virtual = preço_estante_virtual_2.get_text()

            link_estante_virtual = sopa_estante_virtual.find_all('div', {'class': 'ver-livros'})

            link_estante_virtual = link_estante_virtual[i]

            carrinho_estante_virtual = link_estante_virtual.find('a')

            if nome_do_livro.lower() in trocar_caracter(nome_estante_virtual.lower()):
                pass
        
        print('__________________________________________________________________________')

        print(f'\n___ESTANTE VIRTUAL___ \n')

        print(f'--nome-- \n{nome_estante_virtual.strip()} \n \n--preço-- \n{preço_estante_virtual.strip()} \n')

        print('url:', 'www.estantevirtual.com.br' + carrinho_estante_virtual.get('href'))    
        
        # nome_estante_virtual = 'nao encontrado'

        # preço_estante_virtual = 'nao encontrado'

except AttributeError and IndexError:

    print('__________________________________________________________________________')

    print(f'\n___ESTANTE VIRTUAL___ \n')

    print('--NÃO ENCONTRADO--')

    nome_estante_virtual = 'nao encontrado'

    preço_estante_virtual = 'nao encontrado'


'''LIVRARIA CULTURA'''

pagina_livraria_cultura = get(url['livraria_cultura'])

sopa_livraria_cultura = BeautifulSoup(pagina_livraria_cultura.content, 'html.parser')

#TESTAR ERRO

try:
    
    pesquisa_livraria_cultura = 'LIVRARIA CULTURA'

    nome_livraria_cultura = sopa_livraria_cultura.find('h2', {'class' : 'prateleiraProduto__informacao__nome'}).get_text()

    preço_livraria_cultura = sopa_livraria_cultura.find('span', {'class' : 'prateleiraProduto__informacao__preco--por'}).get_text()

    link_livraria_cultura = sopa_livraria_cultura.find('h2', {'class': 'prateleiraProduto__informacao__nome'})

    carrinho_livraria_cultura = link_livraria_cultura.find('a')

    if nome_do_livro.lower() in trocar_caracter(nome_livraria_cultura.lower()):

        print('__________________________________________________________________________')

        print(f'\n___LIVRARIA CULTURA___ \n')

        print(f'--nome-- \n{nome_livraria_cultura.strip()} \n \n--preço-- \n{preço_livraria_cultura.strip()} \n')

        print('url:', 'www.estantevirtual.com.br' + carrinho_livraria_cultura.get('href'))

    else: 
        i=1
        # nome_livraria_cultura = 'nao encontrado'

        # preço_livraria_cultura = 'nao encontrado'
        
        while nome_do_livro.lower() not in trocar_caracter(nome_livraria_cultura.lower()):
            i+=1
            nomes_livraria_cultura = sopa_livraria_cultura.find_all('h2', {'class' : 'prateleiraProduto__informacao__nome'})

            nome_livraria_cultura_2 = nomes_livraria_cultura[i]

            nome_livraria_cultura = nome_livraria_cultura_2.get_text()

            #verificação(text_nome_livraria_cultura_2)

            preço_livraria_cultura = sopa_livraria_cultura.find_all('span', {'class' : 'prateleiraProduto__informacao__preco--valor'})

            preço_livraria_cultura_2 = preço_livraria_cultura[i]

            preço_livraria_cultura = preço_livraria_cultura_2.get_text()

            link_livraria_cultura = sopa_livraria_cultura.find_all('h2', {'class': 'prateleiraProduto__informacao__nome'})

            link_livraria_cultura = link_livraria_cultura[i]

            carrinho_livraria_cultura = link_livraria_cultura.find('a')

            if nome_do_livro.lower() in trocar_caracter(nome_livraria_cultura.lower()):
                pass
        
        print('__________________________________________________________________________')

        print(f'\n___LIVRARIA CULTURA___ \n')

        print(f'--nome-- \n{nome_livraria_cultura.strip()} \n \n--preço-- \n{preço_livraria_cultura.strip()} \n')

        print('url:', carrinho_livraria_cultura.get('href'))


        

        
        '''
        print('__________________________________________________________________________')

        print(f'\n___LIVRARIA CULTURA___ \n')

        print('--NÃO ENCONTRADO--')
        '''


except AttributeError and IndexError:

    print('__________________________________________________________________________')

    print('\n___LIVRARIA CULTURA___ \n')

    print('--NÃO ENCONTRADO--')

    nome_livraria_cultura = 'nao encontrado'

    preço_livraria_cultura = 'nao encontrado'

'''LIVRARIA LEITURA'''

pagina_livraria_leitura = get(url['livraria_leitura'])

sopa_livraria_leitura = BeautifulSoup(pagina_livraria_leitura.content, 'html.parser')



try:

    pesquisa_livraria_leitura = 'LIVRARIA LEITURA'

    nome_livraria_leitura = sopa_livraria_leitura.find('h4').get_text()
    
    preço_livraria_leitura = 'não encontrado'
    elemento_preço = sopa_livraria_leitura.find('span', {'class' : 'price-new'})
    if elemento_preço is not None:
        preço_livraria_leitura = elemento_preço.get_text()

    link_livraria_leitura = sopa_livraria_leitura.find('div', {'class' : 'caption'})

    carrinho_livraria_leitura = link_livraria_leitura.find('a')

    if nome_do_livro.lower() in trocar_caracter(nome_livraria_leitura.lower()):

        print('__________________________________________________________________________')

        print(f'\n___LIVRARIA LEITURA___ \n')

        print(f'--nome-- \n{nome_livraria_leitura.strip()} \n \n--preço-- \n{preço_livraria_leitura.strip()} \n')

        print('url:', carrinho_livraria_leitura.get('href'))

    else: 
        i=1
        
        while nome_do_livro.lower() not in trocar_caracter(nome_livraria_leitura.lower()):
            i+=1
            nomes_livraria_leitura = sopa_livraria_leitura.find_all('h4')

            nome_livraria_leitura_2 = nomes_livraria_leitura[i]

            nome_livraria_leitura = nome_livraria_leitura_2.get_text()

            #verificação(text_nome_livraria_leitura_2)

            preço_livraria_leitura = sopa_livraria_leitura.find_all('span', {'class' : 'price-new'})

            preço_livraria_leitura_2 = preço_livraria_leitura[i]

            preço_livraria_leitura = preço_livraria_leitura_2.get_text()

            link_livraria_leitura = sopa_livraria_leitura.find_all('div', {'class': 'caption'})

            link_livraria_leitura = link_livraria_leitura[i]

            carrinho_livraria_leitura = link_livraria_leitura.find('a')

            if nome_do_livro.lower() in trocar_caracter(nome_livraria_leitura.lower()):
                pass
        
        print('__________________________________________________________________________')

        print(f'\n___LIVRARIA LEITURA___ \n')

        print(f'--nome-- \n{nome_livraria_leitura.strip()} \n \n--preço-- \n{preço_livraria_leitura.strip()} \n')

        print('url:', carrinho_livraria_leitura.get('href'))


except AttributeError and IndexError:

    print('__________________________________________________________________________')

    print('\n___LIVRARIA LEITURA___ \n')

    print('--NÃO ENCONTRADO--')

    nome_livraria_leitura = 'nao encontrado'

    preço_livraria_leitura = 'nao encontrado'

'''lIVRARIA DA VILA'''

pagina_livraria_da_vila = get(url['livraria_da_vila'])

sopa_livraria_da_vila = BeautifulSoup(pagina_livraria_da_vila.content, 'html.parser')

#TESTAR ERRO

try:

    pesquisa_livraria_da_vila = 'LIVRARIA DA VILA'

    nome_livraria_da_vila = sopa_livraria_da_vila.find('div', {'class':'prod-nome'}).get_text()

    preço_livraria_da_vila = 'não encontrado'
    elemento_preço = sopa_livraria_da_vila.find('div', {'class':'price'})
    if elemento_preço is not None:
        preço_livraria_da_vila = elemento_preço.get_text()


    link_livraria_da_vila = sopa_livraria_da_vila.find('div', {'class':'prod-nome'})

    carrinho_livraria_da_vila = link_livraria_da_vila.find('a')

    if nome_do_livro.lower() in trocar_caracter(nome_livraria_da_vila.lower()):
        print('__________________________________________________________________________')

        print(f'\n___LIVRARIA DA VILA___ \n')

        print(f'--nome-- \n{nome_livraria_da_vila.strip()} \n \n--preço-- \n{preço_livraria_da_vila.strip()} \n')

        print('url:', carrinho_livraria_da_vila.get('href'))

    else: 
        i=1
        
        while nome_do_livro.lower() not in trocar_caracter(nome_livraria_da_vila.lower()):
            i+=1
            nomes_livraria_da_vila = sopa_livraria_da_vila.find_all('div', {'class':'prod-nome'})

            nome_livraria_da_vila_2 = nomes_livraria_da_vila[i]

            nome_livraria_da_vila = nome_livraria_da_vila_2.get_text()

            #verificação(text_nome_livraria_da_vila_2)

            preço_livraria_da_vila = sopa_livraria_da_vila.find_all('div', {'class':'price'})

            preço_livraria_da_vila_2 = preço_livraria_da_vila[i]

            preço_livraria_da_vila = preço_livraria_da_vila_2.get_text()

            link_livraria_da_vila = sopa_livraria_da_vila.find_all('div', {'class':'prod-nome'})

            link_livraria_da_vila = link_livraria_da_vila[i]

            carrinho_livraria_da_vila = link_livraria_da_vila.find('a')

            if nome_do_livro.lower() in trocar_caracter(nome_livraria_da_vila.lower()):
                pass
        

        print('__________________________________________________________________________')

        print(f'\n___LIVRARIA DA VILA___ \n')

        print(f'--nome-- \n{nome_livraria_da_vila.strip()} \n \n--preço-- \n{preço_livraria_da_vila.strip()} \n')

        print('url:', carrinho_livraria_da_vila.get('href'))

except AttributeError and IndexError:

    print('__________________________________________________________________________')

    print('\n___LIVRARIA DA VILA___ \n')

    print('--NÃO ENCONTRADO--')

    print('__________________________________________________________________________')

    nome_livraria_da_vila = 'nao encontrado'

    preço_livraria_da_vila = 'nao encontrado'

'''PARTE CSV'''

#AJUSTE PREÇO

preço_estante_virtual = trocar_caracter(preço_estante_virtual).strip()
preço_livraria_cultura = trocar_caracter(preço_livraria_cultura).strip()
preço_livraria_leitura = trocar_caracter(preço_livraria_leitura).strip()
preço_livraria_da_vila = trocar_caracter(preço_livraria_da_vila).strip()

#AJUSTE NOME

nome_estante_virtual = trocar_caracter(nome_estante_virtual).strip().lower()
nome_livraria_cultura = trocar_caracter(nome_livraria_cultura).strip().lower()
nome_livraria_leitura = trocar_caracter(nome_livraria_leitura).strip().lower()
nome_livraria_da_vila = trocar_caracter(nome_livraria_da_vila).strip().lower()

with open('banco_csv.csv', 'a', newline='') as arquivo:
    escrever = csv.writer(arquivo)
    escrever.writerow([nome_estante_virtual, preço_estante_virtual, nome_livraria_cultura, preço_livraria_cultura, nome_livraria_leitura, preço_livraria_leitura, nome_livraria_da_vila, preço_livraria_da_vila])