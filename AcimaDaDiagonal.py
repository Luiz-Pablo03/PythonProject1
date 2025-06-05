operacao = str(input())

matriz= []

for linha_da_matriz in range(12):
    nova_linha = []
    for coluna_da_matriz in range(12):
        elemento = float(input())
        nova_linha.append(elemento)
    matriz.append(nova_linha)

contador = 0
soma = 0

for l in range(12):
    for c in range(12):
        if c > l:
            soma += matriz[l][c]
            contador += 1

if operacao == 'S':
    resultado = soma
    print(f"{resultado:.1f}")

elif operacao == 'M':
    resultado = soma/contador
    print(f"{resultado:.1f}")
