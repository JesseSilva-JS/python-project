# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

#import
import random 
from os import system, name 

#Função para limar a tela a cada execução

def limpa_tela():

    #Windows
    if name == 'nt':
        _ = system('cls')

    #mac ou linux
    else:
        _ = system('clear')

def game():

    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca')
    print('Adivinhe a palavra abaixo: \n')

    #lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #escolhe randomicamente uma palavra            
    palavra = random.choice(palavras)

    #list comprehesion
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    #lista para as letras erradas
    letras_erradas = []

    #Loop enquanto número de chances for maior do que zero
    while chances > 0 :
        #print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", "".join(letras_erradas))


        #Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        #condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palbra era:", palavra)    
            break

    #condicional 
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)


#bloco main

if __name__ == "__main__":
    game()
    print("\n Parabéns. Você está aprendendo programação em Python com a Data Science Academy :)\n")