N = int(input())
M = int(input())

# Cria um conjunto (set) para armazenar os números das figurinhas que já tem.
# Um conjunto só armazena valores únicos, oq resolve o problema das figs repetidas
figurinhas_que_tenho = set()

for blablabla in range(M):
    # Lê o número da figurinha.
    numero_figurinha = int(input())
    # Adiciona o número ao conjunto. Se o número já existir, nada acontece (eu acho)
    figurinhas_que_tenho.add(numero_figurinha)

# O número de figurinhas únicas que temos é o tamanho do conjunto
numero_de_figurinhas_unicas = len(figurinhas_que_tenho)

# O número de figurinhas que faltam é o total do álbum menos as que já temos.
figurinhas_faltantes = N - numero_de_figurinhas_unicas

print(figurinhas_faltantes)
