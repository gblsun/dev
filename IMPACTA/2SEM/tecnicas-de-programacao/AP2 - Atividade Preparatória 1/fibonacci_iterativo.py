def fibonacci_iterativo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    anterior, atual = 0, 1
    for _ in range(3, n + 1):
        anterior, atual = atual, anterior + atual
    return atual
