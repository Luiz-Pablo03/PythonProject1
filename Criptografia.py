# Função para criptografar UMA ÚNICA linha de texto
def criptografar(mensagem_original):
    # --- PASSADA 1 ---
    mensagem_passada1 = ""
    for caractere in mensagem_original:
        # Verifica se é uma letra do alfabeto
        if 'a' <= caractere <= 'z' or 'A' <= caractere <= 'Z':
            # Desloca 3 posições para a direita
            mensagem_passada1 += chr(ord(caractere) + 3)
        else:
            # Mantém o caractere original se não for letra
            mensagem_passada1 += caractere

    # --- PASSADA 2 ---
    # Inverte a string resultante da passada 1
    mensagem_passada2 = mensagem_passada1[::-1]

    # --- PASSADA 3 ---
    tamanho = len(mensagem_passada2)
    meio = tamanho // 2

    # Separa a string em duas metades
    primeira_metade = mensagem_passada2[:meio]
    segunda_metade = mensagem_passada2[meio:]

    nova_segunda_metade = ""
    for caractere in segunda_metade:
        # Desloca cada caractere da segunda metade 1 posição para a esquerda
        nova_segunda_metade += chr(ord(caractere) - 1)

    # Junta a primeira metade (inalterada) com a segunda metade (modificada)
    mensagem_final = primeira_metade + nova_segunda_metade

    return mensagem_final


# Leitura do número de casos de teste
N = int(input())

# Loop para processar cada caso de teste
for l in range(N):
    linha_para_criptografar = input()
    resultado = criptografar(linha_para_criptografar)
    print(resultado)
