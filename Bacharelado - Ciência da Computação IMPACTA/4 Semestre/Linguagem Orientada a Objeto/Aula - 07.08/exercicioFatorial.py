# 2. Calcular o fatorial de um número usando loop do-while (ou equivalente em Python)
n = int(input("Digite um valor para calcular fatorial: "))


i = 0
while (n > 0):
    i += 1
    fatorial = n * (n - i)
    break
# n = 5
# 
print(fatorial)