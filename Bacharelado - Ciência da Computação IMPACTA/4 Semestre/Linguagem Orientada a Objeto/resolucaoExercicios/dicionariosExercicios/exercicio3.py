'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+

Exercício 03
Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogal aparece no texto. 

A função deve receber o texto como entrada e retornar o dicionário.

Exemplo:
Para o texto abaixo:
texto = ' faculdade impacta de tecnologia'
A função deve devolver o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o' : 2, 'i': 2 }'''

def contadorVogal(frase):
    frase = frase.lower()
    contA = 0
    contE = 0
    contI = 0
    contO = 0
    contU = 0
    for caractere in frase:
        if 'a' == caractere:
            contA+=1
        if 'e' == caractere:
            contE+=1
        if 'i' == caractere:
            contI+=1
        if 'o' == caractere:
            contO+=1
        if 'u' == caractere:
            contU+=1
    dicionario = dict([
    ('a', contA),
    ('e', contE),
    ('i', contI),
    ('o', contO),
    ('u', contU)
    ])
    return dicionario

frase = input("Digite a frase: ")
print(contadorVogal(frase))







