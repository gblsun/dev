'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
Exercício resolvido dia 08/08/2025.'''
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