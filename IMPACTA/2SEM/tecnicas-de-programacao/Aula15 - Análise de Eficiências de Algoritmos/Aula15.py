'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Aula 15: técnicas de programação IMPACTA 27 de Setembro de 2024                      |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
→ 
↳

Análise de eficiência
    de algoritmos

→ Geralmente temos várias soluções possíveis para
um dado problema.
    ↳ Como compará-las?
    ↳ Qual a mais eficiente?
→ Possíveis critérios de comparação:
    ↳ Tempo de execução
    ↳ Uso de memória


→ Como medir o tempo de execução?
Medimos o tempo contando a quantidade de passos/instruções que são executados pelo algoritmo
    ↳ Atenção: não confundir quantidade de passos com
linhas de código
    ↳ Pode variar de acordo com a entrada do algoritmo
→ Cronometrar o tempo no relógio não é uma boa
alternativa
→ Depende de diferentes fatores:
    ↳ Hardware
    ↳ Memória disponível
    ↳ Compilador
    ↳ Linguagem de programação
'''
#%% ---> begin
# seria executado 200 vezes independente do hardware, independete do software, independete da linguagem e IDE.
    for i in range(10):
        for j in range(20):
            if i*j==100:
                break
            print(i*j)
#%% ---> end
# qtd de linhas ≠ qtd de instruções ou qtd de passos.
'''
Pode variar de acordo com a entrada do algoritmo, portanto:
'''
#%%

# → Algoritmo a:
x = x + 1

# → Algoritmo b:
for i in range(0, n):
x = x + 1

# → Algoritmo c:
for i in range(0, n):
    for j in range(0, n):
    x = x + 1

'''
Algoritmo a: instrução executada 1 vez
Algoritmo b: instrução executada n vezes
Algoritmo c: instrução executada n² vezes

1, n e n² são chamados ordens de grandeza ou ordens de complexidade


Notação O grande (Big O)

→ É a notação mais conhecida para descrever o desempenho de um algoritmo. Indica o quão rápido ele é.

→ Ao analisarmos um algoritmo devemos analisar o pior caso do algoritmo, ou seja, a situação em que haverá o maior número de instruções a serem executadas;

→ O tempo de execução nunca ultrapassará esse limite.

+------------+----------------+-------------------------+
| Complexidade |  Classe       | Tempo de Execução      |
+------------+----------------+-------------------------+
| O(1)       |  constante      | ↑ Mais rápido          |
| O(log n)   |  logarítmica    |                        |
| O(log²n)   |  log-quadrática |                        |
| O(n)       |  linear         |                        |
| O(n log n) |  n log n        |                        |
| O(n²)      |  quadrática     |                        |
| O(n³)      |  cúbica         |                        |
| O(2ⁿ)      |  exponencial    |                        |
| O(n!)      |  fatorial       | ↓ Menos rápido         |
+------------+----------------+-------------------------+


'''