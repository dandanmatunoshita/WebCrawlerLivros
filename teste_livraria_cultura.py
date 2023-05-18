import csv
from requests import *
from bs4 import BeautifulSoup

url = {
    'livraria_cultura' : 'https://www3.livrariacultura.com.br/busca/?ft=eu%20robo&originalText=eu%20robo',
}

pagina_livraria_cultura = get(url['livraria_cultura'])

sopa_livraria_cultura = BeautifulSoup(pagina_livraria_cultura.content, 'html.parser')

nomes_livraria_cultura = sopa_livraria_cultura.find_all('h2')

nome_livraria_cultura_2 = nomes_livraria_cultura[2]

text_nome_livraria_cultura_2 = nome_livraria_cultura_2.get_text()

#verificação(text_nome_livraria_cultura_2)

preço_livraria_cultura = sopa_livraria_cultura.find_all('span', {'class' : 'prateleiraProduto__informacao__preco--valor'})

preço_livraria_cultura_2 = preço_livraria_cultura[2]

text_preço_livraria_cultura_2 = preço_livraria_cultura_2.get_text()

link_livraria_cultura = sopa_livraria_cultura.find_all('h2', {'class': 'prateleiraProduto__informacao__nome'})

link_livraria_cultura = link_livraria_cultura[1]

carrinho_livraria_cultura = link_livraria_cultura.find('a')




        #PRINTAR
        
print('__________________________________________________________________________')

print('\n___LIVRARIA CULTURA ___ \n')

print(f'---Nome--- \n{text_nome_livraria_cultura_2.strip()} \n \n---Preço--- \n{text_preço_livraria_cultura_2} \n')
        
print('url:', carrinho_livraria_cultura.get('href'))
