def printar(nome_vetor, vetor):
    for i in range(len(vetor)):
        print(f"{nome_vetor}[{i}] = {vetor[i]}")

par = []
impar = []

for i in range(15):
    number = int(input())
    if number % 2 == 0:
        if len(par) == 5:
            printar("par", par)
            par = []
            par.append(number)
        else:
            par.append(number)
    else:
        if len(impar) == 5:
            printar("impar", impar)
            impar = []
            impar.append(number)
        else:
            impar.append(number)

printar("impar", impar)
printar("par", par)
