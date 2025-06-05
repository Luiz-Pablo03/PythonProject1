
def resolucao(nao_importa):
    # Lê a linha inteira de texto (a frase com várias palavras) do caso de teste atual.
    # O str() é redundante aqui, pois input() já retorna uma string.
    frase_input = input()

    # Divide a string 'frase_input' em uma lista de strings (palavras).
    # Por padrão, .split() separa a string pelos espaços em branco.
    lista_de_palavras = frase_input.split()

    # Define o tamanho máximo que uma palavra pode ter, conforme o enunciado do problema (1 a 50 caracteres).
    tamanho_max_da_palavra = 50

    # Cria a estrutura para agrupar as palavras por tamanho.
    # 'separacao_de_palavras' será uma lista de listas.
    # Cada sublista interna em separacao_de_palavras[X] guardará as palavras que têm tamanho 'X', com X sendo um numero qualquer.
    # A list comprehension [[] for j in range(tamanho_max_da_palavra + 1)]
    # cria 'tamanho_max_da_palavra + 1' (ou seja, 51) listas vazias.
    # Isso prepara "gavetas" para palavras de tamanho 0 até 50, tipo deixando listas prontas para quando houver uma palavra com um size correspondente ao seu índice.
    separacao_de_palavras = [[] for j in range(tamanho_max_da_palavra + 1)]

    # Itera sobre cada palavra na lista original de palavras (mantendo a ordem original).
    for palavra in lista_de_palavras:
        # Obtém o tamanho (comprimento) da palavra atual.
        size = len(palavra)

        # Adiciona a 'palavra' na "gaveta" (sublista) correspondente ao seu 'size'.
        # Ex: se a palavra é "gato" (size=4), ela é adicionada a separacao_de_palavras[4].
        # Como iteramos na ordem original das palavras, a estabilidade da ordenação é mantida
        # para palavras de mesmo tamanho (elas entram na sublista na ordem em que apareceram).
        separacao_de_palavras[size].append(palavra)

    # Inicializa uma lista vazia para armazenar o resultado final ordenado.
    lista_final_ordenada = []

    # Itera pelos tamanhos possíveis de palavra, começando do maior (tamanho_max_da_palavra)
    # até o menor (1), em ordem decrescente.
    # range(start, stop, step): aqui, start=50, stop=0 (não inclusivo), step=-1.
    for size in range(tamanho_max_da_palavra, 0, -1):
        # Adiciona todas as palavras da "gaveta" do tamanho 'size' atual
        # ao final da 'lista_final_ordenada'.
        # O metodo .extend() é usado para adicionar todos os elementos de uma lista em uma string só, diferente do .append
        # (neste caso, separacao_de_palavras[size]) a outra lista.
        # Como as palavras dentro de separacao_de_palavras[size] já estão na ordem estável,
        # e estamos processando os tamanhos em ordem decrescente,
        # a lista_final_ordenada é construída corretamente.
        lista_final_ordenada.extend(separacao_de_palavras[size])

    # Junta todas as palavras da 'lista_final_ordenada' em uma única string,
    # usando um espaço em branco (" ") como separador entre elas.
    resultado_final = " ".join(lista_final_ordenada)

    # Imprime a string resultante, que contém as palavras ordenadas.
    print(resultado_final)


# Leitura do número de casos de teste.
N = int(input())

# Loop para executar a função 'resolucao' para cada caso de teste.
for i in range(N):
    # O argumento passado aqui para 'resolucao' não é usado pela função.
    resolucao(None)  # Passando None ou qualquer valor, já que não é usado.
