def desembaralhador(string):

    size = len(string)
    mid =  size // 2
    first_half = string[0:mid]
    second_half = string[mid:size]

    first_origin = first_half[: : -1]
    second_origin = second_half[: : -1]

    return first_origin + second_origin

N = int(input())

for i in range(N):
    string = str(input())

    string_decrypted = desembaralhador(string)
    print(string_decrypted)
