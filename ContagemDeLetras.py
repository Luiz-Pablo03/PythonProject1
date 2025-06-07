N = int(input())

for b in range(N):
    frase = input()
    frase_minuscula = frase.lower()

    # Cria um contador para cada letra do alfabeto ('a' ate 'z')
    contagem_letras = [0] * 26

    # Coisa o contador
    for caractere in frase_minuscula:
        if 'a' <= caractere <= 'z':
            indice = ord(caractere) - ord('a')
            contagem_letras[indice] += 1

    # Acha a maior frequência que tiver\
    frequencia_maxima = 0
    # any() retorna True se algum elemento da lista nao for zero, nao consegui fazer sem usar isso
    if any(contagem_letras):
        frequencia_maxima = max(contagem_letras)

    # Constrói a string de resultado com as letras mais frequentes apresentadas
    resultado = ""
    for ka in range(26):
        if contagem_letras[ka] == frequencia_maxima:
            resultado += chr(ka + ord('a'))

    print(resultado)
