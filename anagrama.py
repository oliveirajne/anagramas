import re

opcao = 1

def get_anagrama(palavra, linha):

    if sorted(palavra) == sorted(linha):
        print(linha)

def validado(palavra):

    match = re.search('[()[\]{}|//\W.^$*+?0-9ÇÁÀÃÄÉÈÊËÍÌÎÏÓÒÕÖÚÙÛÜ^\s]', palavra)

    if match:
        return False
    else:
        return True


while True:
    
    palavra = input('Digite a palavra para cálculo de anagrama: ')

    palavra = palavra.upper()

    
    if validado(palavra): 

        with open('palavras.txt', 'r') as file:

            for i, linha in enumerate(file):

                linha = linha.rstrip('\n')
                get_anagrama(palavra, linha)
    else:
        print('ERRO! caracteres não permitidos')
        break


