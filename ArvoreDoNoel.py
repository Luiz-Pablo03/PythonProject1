while True:
    try:

        N = int(input())

        # "Desenha" as Folhas
        for numero_asteristicos in range(1, N + 1, 2):
            # Calcula o número de espaços para centralizar a linha atual
            num_espacos = (N - numero_asteristicos) // 2
            # Constrói e imprime a linha com espaços e asteriscos e oq precisar
            print(' ' * num_espacos + '*' * numero_asteristicos)

        # Desenho do tronco
        # Linha do tronco com 1 asteristico
        num_espacos_tronco1 = (N - 1) // 2
        print(' ' * num_espacos_tronco1 + '*')

        # Linha do tronco com 3 asteristicos
        num_espacos_tronco2 = (N - 3) // 2
        print(' ' * num_espacos_tronco2 + '***')
        print()

    except EOFError:
        # Quando não há mais entrada para ler, o 'input()' causa um EOFError.
        break;
