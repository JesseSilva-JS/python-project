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

# Função que desenha a forca na tela
def display_hangman(chances):      
    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]    

def game():

    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca')
    print('Adivinhe a palavra abaixo: \n')

    #lista de palavras para o jogo
    palavras = [
    "Maçã",
    "Banana",
    "Laranja",
    "Pera",
    "Uva",
    "Morango",
    "Abacaxi",
    "Melancia",
    "Limão",
    "Manga",
    "Cereja",
    "Kiwi",
    "Pêssego",
    "Abacate",
    "Framboesa",
    "Amora",
    "Goiaba",
    "Caju",
    "Coco",
    "Tangerina",
    "Maracujá",
    "Pitanga",
    "Jabuticaba",
    "Ameixa",
    "Açaí",
    "Acerola",   
    "Groselha",
    "Caqui",    
    "Pomelo",
    "Figo",
    "Papaya",    
    "Mamão",
    "Carambola",    
    "Guaraná",    
    "Romã",
    "Melão",    
    "Jambo",
    "Tâmara",     
    "Tamarindo",
    "Noz-moscada",
    "Sapoti"
]

    #escolhe randomicamente uma palavra            
    palavra = random.choice(palavras).lower()

    print("A dica é: FRUTA\n")
    
    #list comprehesion
    lista_letras_palavras = [letra for letra in palavra]

    #Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6

    #lista para as letras digitadas
    letras_tentativas = []

    #Loop enquanto número de chances for maior do que zero
    while chances > 0 :

        #print
        print(display_hangman(chances))
        print("\nPalavra: ", tabuleiro)
        print("\n")

        #Tentativa
        tentativa = input("\nDigite uma letra: ")

        #condicional
        if tentativa in letras_tentativas:
            print('Você já tentou essa letra. Escolha outra!')
            continue

        #lista de tentativas (letras)
        letras_tentativas.append(tentativa)    

        #condicional
        if tentativa in lista_letras_palavras:
            print("\nVocê acertou a letra!")    

            #loop
            for indice in range(len(lista_letras_palavras)):
                #condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            #se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro: 
                print('\nVocê venceu! aA palavra era: {}'.format(palavra))
                break
        else:
            print('Ops. Essa letra não está na palavra!')
            #decremento
            chances -= 1           
                    
           

    #condicional 
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}".format(palavra))


#bloco main

if __name__ == "__main__":
    game()
    print("\n Parabéns. Você está aprendendo programação em Python com a Data Science Academy :)\n")