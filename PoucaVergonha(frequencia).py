T = int(input())

for ui in range(T):
    N = int(input())
    nomes = input().split()
    registros = input().split()

    faltosos = []

    # Itera sobre cada aluno e seu respectivo registro
    for i in range(N):
        nome = nomes[i]
        registro = registros[i]

        total_p = 0  # Total de presenças ('P')
        total_a = 0  # Total de ausências ('A')

        # Itera sobre cada caractere no registro de um aluno
        for c in registro:
            if c == 'P':
                total_p += 1
            elif c == 'A':
                total_a += 1

        # Calcula o total de dias letivos registrados (excluindo dispensas 'M')
        total = total_p + total_a

        # Calcula a frequência, evitando divisão por zero
        if total == 0:
            frequencia = 1.0
        else:
            frequencia = total_p / total

        # Se a frequência for menor que 75%, adiciona o nome à lista
        if frequencia < 0.75:
            faltosos.append(nome)

    print(" ".join(faltosos))
