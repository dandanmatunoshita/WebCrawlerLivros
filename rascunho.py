def trocar_caracter(nome):

    acentos = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'ç': 'c', 'Á': 'A', 'À': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A', 'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E', 'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O', 'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ç': 'C'}
    texto_sem_acentos = ''

    for caracter in nome:
        if caracter in acentos:
            texto_sem_acentos += acentos[caracter]

        else:
            texto_sem_acentos += caracter

    nome = texto_sem_acentos

    return nome

def verificação(variavel):
    variavel = trocar_caracter(nome).lower().replace(',', '')
    print(variavel)
    if nome not in variavel:
        print(AttributeError)

nome = 'eduardo'
eduardo = 'Eduardo, o caçador'

print(verificação(eduardo))