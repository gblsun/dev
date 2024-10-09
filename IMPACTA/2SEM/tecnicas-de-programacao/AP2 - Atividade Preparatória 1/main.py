'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| AP2 - Atividade Preparatória 1: técnicas de programação                              |
| IMPACTA 10 de Setembro de 2024 - entrega para 10/10                                  |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
→ 
↳


O objetivo deste exercício é implementar duas abordagens para calcular a sequência de Fibonacci: uma abordagem recursiva e outra iterativa. Em seguida, você irá avaliar empiricamente a complexidade de cada algoritmo, contando o número de iterações ou chamadas realizadas durante a execução.

I. Implemente a função fibonacci_recursivo(n), que retorna o n-ésimo número de Fibonacci usando a abordagem recursiva. A função deve também contar e retornar o número de chamadas feitas durante o cálculo.

    ✔

II. Implemente a função fibonacci_iterativo(n), que retorna o n-ésimo número de Fibonacci usando a abordagem iterativa. A função deve também contar e retornar o número de iterações realizadas durante o cálculo.

    ✔
    
III. No programa principal, teste ambas as funções para valores de  n variando de 1 a 10 (ou um intervalo maior se preferir) e armazene o número de iterações/chamadas realizadas para cada valor de n em um dicionário com o seguinte formato:
{n: qtde de iterações/chamadas}

    ✔

IV. Use a biblioteca matplotlib para plotar gráficos que representem a relação entre n e o número de iterações/chamadas para ambas as abordagens. No gráfico, o eixo x deve representar o valor de n e o eixo y deve representar o número de iterações/chamadas. Veja o exemplo de código anexado na aula 15 se necessário.

V. Pesquise pela complexidade teórica das funções e compare os resultados obtidos. Discuta como o número de iterações ou chamadas muda à medida que n aumenta e como isso reflete na complexidade dos algoritmos.
Aplique a técnica de memoização à função recursiva e analise novamente a complexidade. Discuta a respeito do resultado obtido.
'''
# %% ---> início
# imports
import numpy as np
import matplotlib.pyplot as plt
from fibonacci_recursivo import fibonacci_recursivo 
from fibonacci_iterativo import fibonacci_iterativo



# ---> testes das funções:
# ------> Abordagem recursiva e 
# ---------> Abordagem iterativa 

resultados = {}

# Testando a função recursiva
for n in range(1, 11):
    global chamadas_recursivas
    chamadas_recursivas = 0  # Reseta a contagem de chamadas
    fibonacci_recursivo(n)   # Chama a função
    resultados[n] = chamadas_recursivas  # Armazena o número de chamadas

# Testando a função iterativa
for n in range(1, 11):
    valor, iteracoes = fibonacci_iterativo(n)  # Chama a função
    resultados[n] = resultados.get(n, 0), iteracoes  # Atualiza o dicionário

print(resultados)
# %%
