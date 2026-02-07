"""
Exercício 11 - Desenvolvido por Gabriel Muchon Pavanelli. Faculdade Impacta 21/02/2025.

11 - Desenvolva uma programa em Python que leia os valores de A, B e C de uma
equação do segundo grau e mostre o valor de Delta. (formula Δ = b
2 – 4ac)"""
import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
# print(f'a formula de dalta é igual à {(b*b)-4*(a*c)}\nO valor do x positivo é igual à {(-b+math.sqrt((b*b)-4*(a*c))/2*a)}\nO valor do x negativo é igual à {(-b-math.sqrt((b*b)-4*(a*c))/2*a)}')
delta = ((b*b)-(4*a*c))
raizPositiva = (-b+(math.sqrt(delta))/2*a)
raizNegativa = (-b-(math.sqrt(delta))/2*a)
print(f'A fórmula de delta é igual a {delta}\nO valor da raiz positiva é igual à {raizPositiva}\nO valor da raiz negativa é igual à {raizNegativa}')