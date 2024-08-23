# Aula 6: técnicas de programação IMPACTA 23 de Agosto de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)
# %% --begin

# Recursividade

# Muitos problemas têm a seguinte propriedade: cada instância do problema contém uma instância menor do mesmo problema.
# Dizemos que esses problemas têm estrutura recursiva;
# A ideia básica de um algoritmo recursivo consiste em diminuir sucessivamente o problema em um problema menor, até que o tamanho do problema permita resolvê-lo diretamente;
# Quando isso ocorre, diz-se que o algoritmo atingiu uma condição de parada.

# Recursividade em funções

# Uma função é chamada de recursiva se o corpo da função chama a própria função, direta ou indiretamente.
# Esse processo ocorre até o algoritmo atingir a condição de parada.
# Sem esta condição de parada, o algoritmo nãopára de chamar a si mesmo, até estourar acapacidade da pilha de memória, o que causa término indesejável do programa.

# %% Exemplo 1

# Suponha que deseja-se calcular a soma de uma lista de números: [1, 3, 5, 7, 9]
# Solução não recursiva:

# # Função
# def soma(lista):
#     soma = 0
#     for i in lista:
#     soma = soma + i
#     return soma
# # Programa principal
# lista = [1, 3, 5, 7, 9]
# print(soma(lista)) # 25

# Programa principal
# lista = [1, 3, 5, 7, 9]
# print(soma(lista)) # 25

# Solução recursiva:
# Função
# def soma(lista):
#     if len(lista) == 1:
#     return lista[0]
#     else:
#     return lista[0] + soma(lista[1:])
# #Programa principal
# lista = [1, 3, 5, 7, 9]
# total = soma(lista)
# print(total)

# %% --end