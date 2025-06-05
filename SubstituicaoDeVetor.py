lista = []

for i in range(10):
    numbers = int(input())
    lista.append(numbers)

for i in range(len(lista)):
    if lista[i] == 0 or lista[i] < 0:
        lista[i] = 1

for i in range(0, 10):
    print(f"X[{i}] = {lista[i]}")
