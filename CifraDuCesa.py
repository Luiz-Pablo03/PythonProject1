N = int(input())

for i in range(N):
    mensagem_codificada = input()

    deslocamento = int(input())

    # String vazia para construir a mensagem decodificada
    mensagem_decodificada = ""

    # Itera sobre cada caractere da mensagem codificada
    for letra_codificada in mensagem_codificada:
        # Mapeia a letra para uma posição de 0 a 25
        posicao_codificada = ord(letra_codificada) - ord('A')

        # Desloca para a esquerda
        posicao_decodificada = posicao_codificada - deslocamento

        # Aplica o módulo 26 para tratar o "wrap-around"
        posicao_final = posicao_decodificada % 26

        # Converte a nova posição de volta para uma letra
        letra_final = chr(posicao_final + ord('A'))

        #A diciona a letra decodificada ao resultado
        mensagem_decodificada += letra_final

    print(mensagem_decodificada)
