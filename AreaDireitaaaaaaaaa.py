m = []
O = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

s = 0
cont = 0
col = 11
for i in range(1, 11):
    for j in range(col, 12):
        s += m[i][j]

    cont += 1
    if i < 5:
        col -= 1
    if i > 5:
        col += 1



med = s / cont
if O == "S":
    print(f'{s:.1f}')

else:
    print(f"{med:.1f}")