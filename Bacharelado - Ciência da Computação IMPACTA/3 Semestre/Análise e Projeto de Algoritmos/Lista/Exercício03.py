""" 
Exercício 3 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 21/02/2025.

3 - Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
"""

nome = input("Nome do funcionário: ")
salario = float(input("Salário: "))
print(f"O funcionário {nome} tem um salário de R${salario:.2f} em junho.")
