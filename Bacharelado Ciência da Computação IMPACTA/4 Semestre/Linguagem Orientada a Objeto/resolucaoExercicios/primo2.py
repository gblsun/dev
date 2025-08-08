# 3. Determinar se um número fornecido pelo usuário é primo
# Outra resolução.

def is_prime(n)
    if n <= 1:
        return False  # números menores ou iguais a 1 não são primos
    if n == 2:
        return True # 2 é primo
    if n %  2 == 0:
        return False 
    
    limite = int(n** 0.5) + 1
    for i in range(3, limite, 2 ):
        if n % i == 0:
            return False
    return True

# Exemplo:
numero = int(input("Digite um número: "))
if is_prime(numero):
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo.")