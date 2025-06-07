# Lê a primeira linha com J e R
linha_entrada = input().split()
J = int(linha_entrada[0])  # Número de jogadores
R = int(linha_entrada[1])  # Número de rodadas

# Lê a segunda linha com os pontos e converte para uma lista de >>>INTEIROS<<<
pontos_da_partida = list(map(int, input().split()))

# O índice 0 será para o Jogador 1, índice 1 para o Jogador 2, índice 2 para o jogador 3...e por ai vai
pontuacoes = [0] * J

for i in range(len(pontos_da_partida)):
    # Descobre a qual jogador este ponto pertence usando o módulo
    indice_do_jogador = i % J

    # Adiciona o ponto à pontuação total do jogador correspondente
    pontuacoes[indice_do_jogador] += pontos_da_partida[i]

pontuacao_maxima = 0
jogador_vencedor = 0

for i in range(J):
    # Se a pontuação do jogador atual for MAIOR OU IGUAL à máxima encontrada até agora -->
    if pontuacoes[i] >= pontuacao_maxima:
        # <---- atualiza a pontuação máxima e guardamos este jogador como o vencedor, fim de papoooooo
        pontuacao_maxima = pontuacoes[i]
        # Guardamos o NÚMERO do jogador (índice + 1)
        jogador_vencedor = i + 1

# Imprime o número do jogador vencedor
print(jogador_vencedor)
# ACABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO