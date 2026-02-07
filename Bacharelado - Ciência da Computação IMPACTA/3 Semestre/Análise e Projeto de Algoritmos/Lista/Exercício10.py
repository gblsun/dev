"""
Exercício 10 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 21/02/2025.

10 - Faça um programa em Python que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo
que cada litro de tinta pinta uma área de 2 metros quadrados."""

largura = float(input("Digite a largura da sua parede: "))
altura = float(input("Digite a altura da sua parede:"))
area = largura * altura
qtdTinta = area / 2
print("Você precisará de: " , qtdTinta , " Litros de tinta.");
