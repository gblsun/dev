'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
Exercício resolvido dia 08/08/2025.'''
# 1. Determinar se um ano fornecido pelo usuário é bissexto ou não
# Um ano é bissexto se for divisível por 4 e, se for divisível por 100, deve ser também divisível por 400.

ano = int(input("Digite um ano: "))
if (ano % 4 == 0) or (( ano % 100 == 0 ) and (ano % 400 == 0)):
    print("O ano:", ano ," digitado é Bissexto. ")
else:
    print("O ano digitado não é Bissexto. ")

