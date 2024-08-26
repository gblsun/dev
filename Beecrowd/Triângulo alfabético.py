n = int(input("Digite um número de 1 - 26"))
if n >= 1 and n <= 26:
    for i in range(1, n + 1):
        caractere = chr(64 + i)
        print(caractere * i)