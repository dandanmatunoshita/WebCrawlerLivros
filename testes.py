nome_livro = input('Nome livro: ')

def testar(nome, preço):

    if nome_livro.lower() in nome.lower():
        print('__________________________________________________________________________')

        print(f'\n___{nome}___ \n')

        print(f'--nome-- \n{nome.strip()} \n \n--preço-- \n{preço} \n')

    else:
        print('Não encontrado')

testar('eduardo', 10)