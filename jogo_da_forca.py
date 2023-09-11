# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão Final

# Importação de bibliotecas
import json
import sys
import random
import re
from os import system, name

# Constante para a mensagem de dica
DICA_MESSAGE = 'A dica é: {}'

# Função para limpar a tela a cada execução
def limpa_tela():
    try:
        # Lógica para limpar a tela (depende do ambiente em que você está executando o código)
        # Windows
        if name == 'nt':
            _ = system('cls')
        # Mac ou Linux
        else:
            _ = system('clear')
    except Exception as e:
        print(f"Erro ao limpar a tela: {e}")

# Função que desenha a forca na tela
def display_hangman(chances):
    try:
        # Lógica para exibir a imagem do enforcado com base nas chances restantes
        stages = [
            # Estágio 6 (final)
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            """,
            # Estágio 5
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
            """,
            # Estágio 4
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
            """,
            # Estágio 3
            """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
            """,
            # Estágio 2
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
            """,
            # Estágio 1
            """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
            """,
            # Estágio 0
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
    except Exception as e:
        print(f"Erro ao exibir imagem do enforcado: {e}")

# Função para validar a entrada do jogador
def validar_entrada(tentativa):
    padrao = r'^[a-zA-Z]$'
    return re.match(padrao, tentativa) is not None

# Função para carregar palavras do arquivo JSON
def carregar_palavras():
    try:
        # Lógica para carregar palavras
        with open('jogo_da_forca/categorias.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except Exception as e:
        print(f"Erro ao carregar palavras: {e}")
        return []

# Função para escolher uma categoria aleatória
def escolher_categoria(palavras):
    try:
        # Lógica para escolher a categoria
        return random.choice(list(palavras.keys()))
    except Exception as e:
        print(f"Erro ao escolher categoria: {e}")
        return "categoria_padrão"

# Função para escolher uma palavra aleatória da categoria
def escolher_palavra(palavras, categoria):
    try:
        # Lógica para escolher a palavra
        return random.choice(palavras[categoria]).lower()
    except Exception as e:
        print(f"Erro ao escolher palavra: {e}")
        return "palavra_padrão"

# Função para processar a jogada do jogador
def handle_turn(chances, tabuleiro, letras_tentadas, lista_letras_palavras, categoria):
    try:
        print(display_hangman(chances))
        print('\nPalavra: ', ' '.join(tabuleiro))
        print(DICA_MESSAGE.format(categoria))
        print('\n')
        sys.stdout.flush()

        tentativa = input('\nDigite uma letra: ').lower()

        if not validar_entrada(tentativa):
            print('Entrada inválida. Por favor, digite apenas uma letra.')
            return chances, False

        if tentativa in letras_tentadas:
            print(DICA_MESSAGE.format(categoria))
            print(letras_tentadas)
            print('Você já tentou essa letra. Escolha outra!')
            return chances, False

        letras_tentadas.append(tentativa)

        if tentativa in lista_letras_palavras:
            print(DICA_MESSAGE.format(categoria))
            print('\nVocê acertou a letra')

            for indice, letra in enumerate(lista_letras_palavras):
                if letra == tentativa:
                    tabuleiro[indice] = letra
            return chances, '_' not in tabuleiro
        else:
            print(DICA_MESSAGE.format(categoria), '\n')
            print(f'\nOps. A letra {tentativa} não está na palavra!')
            print('\nVocê não acertou nenhuma letra nesse turno.')
            chances -= 1
    except Exception as e:
        print(f"Erro durante o jogo: {e}")

    return chances, False

# Função principal do jogo
def game():
    try:
        palavras = carregar_palavras()

        if not palavras:
            print("Não foi possível carregar as palavras. O jogo não pode continuar.")
            return

        categoria = escolher_categoria(palavras)
        palavra_secreta = escolher_palavra(palavras, categoria)

        limpa_tela()

        print('\nBem-vindo(a) ao jogo da forca')
        print('Adivinhe a palavra abaixo: \n')

        print(DICA_MESSAGE.format(categoria))

        lista_letras_palavras = [letra.lower() for letra in palavra_secreta]
        tabuleiro = ['_' if letra != ' ' else ' ' for letra in palavra_secreta]
        chances = 6
        letras_tentadas = []

        while chances > 0:
            chances, ganhou = handle_turn(
                chances, tabuleiro, letras_tentadas, lista_letras_palavras, categoria)
            if ganhou:
                print('\nVocê venceu! A palavra era: {}'.format(palavra_secreta))
                break

        if chances == 0:
            print(display_hangman(chances))
            print('\nVocê perdeu! A palavra era: {}'.format(palavra_secreta))

    except Exception as e:
        print(f"Erro no jogo: {e}")

# Bloco principal
if __name__ == "__main__":
    game()
