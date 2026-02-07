'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
Exercício resolvido dia 08/08/2025.'''
# 3. Determinar se um número fornecido pelo usuário é primo

'''

→ Se o número for menor que 2, ele não é primo.

→ Veja se o número pode ser dividido exatamente por algum número entre 2 e a raiz quadrada dele.

    ↳ Se encontrar algum número que divide exatamente, o número não é primo.

    ↳ Se não encontrar nenhum, o número é primo.

'''
import math

n = int(input("Digite um valor: "))

if n < 2:
    print(n ,'não é primo.')

i = 2
for i in range(2, int(math.sqrt(n)) + 1):

    if n % i == 0:
        print(n, 'não é primo.')
        break

else:
    print(n ,'é primo.')

