# # Aula: técnicas de programação IMPACTA 16 e 17 de Agosta de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Novas estruturas de Dados:
# Dicionários

# Exercício II
# Escreva uma função que conta a quantidade devogais em um texto e armazena tal quantidade emum dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogalaparece no texto. A função deve receber o texto como entrada e retornar o dicionário. Por exemplo, para o texto abaixo: texto = 'faculdade impacta de tecnologia' A função deve devolver o seguinte dicionário:{'a': 5, 'u': 1, 'e': 3, 'o' : 2, 'i': 2 }

# ainda não terminado
# %% ---begin
texto = input("Digite seu texto: ")
vogais = {"a", "e", "i", "o", "u"}
contagem = sum(1 for char in texto.lower() if char in 'a' if char in)
print(contagem)
# %% ---end
