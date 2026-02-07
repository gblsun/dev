'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
Exercício resolvido dia 08/08/2025.'''
# 2. Calcular o fatorial de um número usando loop do-while (ou equivalente em Python)

# n!=n×(n−1)×(n−2)×⋯×2×1
n = int(input('Digite um valor para o cálculo de fatorial: '))
i = n
fatorial = 1

while i > 0:
    fatorial *= i
    i -= 1

print(fatorial)

