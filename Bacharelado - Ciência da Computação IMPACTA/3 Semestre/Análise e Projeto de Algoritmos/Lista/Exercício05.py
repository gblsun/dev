""" 
Exercício 5 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 21/02/2025.

5 - Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5
"""

aluno = input("Digite o nome do aluno: ")
n1 = int(input("Digite a primeira nota do aluno: "))
n2 = int(input("Digite a segunda nota do aluno: "))
media = (n1 + n2) / 2
print(f"Olá {aluno}, a média entre  {n1} e {n2} é igual à {media:.1f}")