# QUESTÃO MAIS LEGAL DA LISTA
N = int(input())

for p in range(N):
    frase = input()
    # Separa a frase em uma lista de palavras, isso eh, literalmente uma lista com as palavras individuais da frase
    lista_de_palavras = frase.split()

    mensagem_oculta = ""

    for palavra in lista_de_palavras:
        # Pega o primeiro caractere (índice 0) da palavra iterada e adiciona ao resultado
        mensagem_oculta += palavra[0]

    print(mensagem_oculta)
