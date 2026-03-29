# Floyd-Warshall: Caminhos Mínimos em Grafos

## Descrição

Este projeto apresenta a implementação do **algoritmo de Floyd-Warshall** em Python, utilizado para calcular os **menores caminhos entre todos os pares de vértices** em um grafo direcionado e ponderado.

A solução inclui:

- Cálculo da matriz de menores distâncias
- Construção automática da matriz de precedência
- Reconstrução de caminhos mínimos
- Visualização do grafo dirigido com pesos

---

## Informações Acadêmicas

- **Disciplina:** Teoria dos Grafos  
- **Curso:** Ciência da Computação — 5º semestre  
- **Professor:** Kyung Moo Kim  
- **Aluno:** Gabriel Muchon Pavanelli  

---

## Objetivo

Demonstrar, de forma prática, o funcionamento do algoritmo de Floyd-Warshall, aplicando conceitos fundamentais de:

- Grafos direcionados
- Programação dinâmica
- Caminhos mínimos
- Representação matricial de grafos

---

## Fundamentação Teórica

O algoritmo de Floyd-Warshall resolve o problema de caminhos mínimos entre todos os pares de vértices.

A cada iteração, verifica-se se um caminho pode ser otimizado passando por um vértice intermediário.

$$
d_{ij}^{(k)} = \min \left( d_{ij}^{(k-1)},\; d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)
$$

---

## Estruturas Utilizadas

### Matriz de Distâncias

Representa o custo direto entre vértices:

- $0$ → mesmo vértice  
- valor numérico → peso da aresta  
- $\infty$ → ausência de aresta (`inf` no código)  

---

### Matriz de Precedência

Armazena o vértice anterior no caminho mínimo:

$$
\pi_{ij}^{(0)} =
\begin{cases}
\text{NIL}, & \text{se } i = j \text{ ou } w_{ij} = \infty \\
i, & \text{caso contrário}
\end{cases}
$$

---

## Complexidade

- **Tempo:** $O(n^3)$  
- **Espaço:** $O(n^2)$  

---

## Entrada de Dados

O usuário deve informar:

1. Número de vértices  
2. Matriz de distâncias  

Formato:

- Valores separados por espaço  
- Utilizar `inf` para indicar ausência de aresta  

Exemplo:
# Floyd-Warshall: Caminhos Mínimos em Grafos

## Descrição

Este projeto apresenta a implementação do **algoritmo de Floyd-Warshall** em Python, utilizado para calcular os **menores caminhos entre todos os pares de vértices** em um grafo direcionado e ponderado.

A solução inclui:

- Cálculo da matriz de menores distâncias
- Construção automática da matriz de precedência
- Reconstrução de caminhos mínimos
- Visualização do grafo dirigido com pesos

---

## Informações Acadêmicas

- **Disciplina:** Teoria dos Grafos  
- **Curso:** Ciência da Computação — 5º semestre  
- **Professor:** Kyung Moo Kim  
- **Aluno:** Gabriel Muchon Pavanelli  

---

## Objetivo

Demonstrar, de forma prática, o funcionamento do algoritmo de Floyd-Warshall, aplicando conceitos fundamentais de:

- Grafos direcionados
- Programação dinâmica
- Caminhos mínimos
- Representação matricial de grafos

---

## Fundamentação Teórica

O algoritmo de Floyd-Warshall resolve o problema de caminhos mínimos entre todos os pares de vértices.

A cada iteração, verifica-se se um caminho pode ser otimizado passando por um vértice intermediário.

$$
d_{ij}^{(k)} = \min \left( d_{ij}^{(k-1)},\; d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)
$$

---

## Estruturas Utilizadas

### Matriz de Distâncias

Representa o custo direto entre vértices:

- $0$ → mesmo vértice  
- valor numérico → peso da aresta  
- $\infty$ → ausência de aresta (`inf` no código)  

---

### Matriz de Precedência

Armazena o vértice anterior no caminho mínimo:

$$
\pi_{ij}^{(0)} =
\begin{cases}
\text{NIL}, & \text{se } i = j \text{ ou } w_{ij} = \infty \\
i, & \text{caso contrário}
\end{cases}
$$

---

## Complexidade

- **Tempo:** $O(n^3)$  
- **Espaço:** $O(n^2)$  

---

## Entrada de Dados

O usuário deve informar:

1. Número de vértices  
2. Matriz de distâncias  

Formato:

- Valores separados por espaço  
- Utilizar `inf` para indicar ausência de aresta  

Exemplo:

0 3 inf 7
8 0 2 inf
5 inf 0 1
2 inf inf 0


---

## Saídas do Programa

O sistema gera:

### Matriz de menores distâncias

[0, 3, 5, 6]
[5, 0, 2, 3]
[3, 6, 0, 1]
[2, 5, 7, 0]

---

### Caminho mínimo entre vértices

Exemplo:

Origem: 0
Destino: 3

Caminho: [0, 1, 2, 3]
Custo: 6


---

### Visualização do grafo

O grafo é exibido com:

- Vértices
- Arestas direcionadas
- Pesos

Utilizando:

- NetworkX  
- Matplotlib  

---

## Como Executar

1. Instale as dependências:

pip install networkx matplotlib

2. Execute o programa:
Execute o programa

Insira os dados solicitados.
-----

/Algoritmo Floyd Warshall
│
├── AtividadeAlgoritmoFloydWarshall.ipynb
└── README.md

### Possíveis Melhorias (To-do)
- Interface gráfica interativa
- Entrada via arquivos
- Destaque visual do caminho mínimo
- Exportação do grafo como imagem

## Conclusão

O algoritmo de Floyd-Warshall é uma abordagem eficiente para determinar caminhos mínimos entre todos os pares de vértices em um grafo.

Sua implementação permite compreender, na prática, conceitos fundamentais de teoria dos grafos e programação dinâmica.