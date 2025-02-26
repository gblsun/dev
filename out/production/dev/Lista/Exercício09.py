"""
Exercício 9 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 21/02/2025.

9 - Faça um programa em Python que leia quanto dinheiro uma pessoa tem na carteira (em
R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45. (ou cotação
atual)"""

reais = float(input("Digite quandos reais você possui: "))
print(f"{reais} convertido em doláres, fica: {reais/5.71 }")