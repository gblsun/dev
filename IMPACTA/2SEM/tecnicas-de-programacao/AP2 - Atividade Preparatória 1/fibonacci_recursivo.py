from functools import lru_cache

@lru_cache
def fibonacci_recursivo(n):
    """
    A função calcula o número de fibonacci recursivamente em Python.
    
    : param n: no trecho de código fornecido, a função `fib (n)` calcula o número de fibonacci do Fibonacci
    recursivamente.A função retorna o número de Fibonacci na posição `n`
    : Return: o código está calculando o 10º número na sequência de Fibonacci usando um recursivo
    função.A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma do
    dois números anteriores.
    """
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fibonacci_recursivo(n-1)+ fibonacci_recursivo(n-2))