# Aula 6: técnicas de programação IMPACTA 23 de Agosto de 2024

#Os números de Fibonacci constituem umasequência de números na qual os dois primeiroselementos são 0 e 1 e os demais, a soma dos dois elementos imediatamente anteriores.
# A sequência formada pelos 10 primeiros números de Fibonacci é: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 definição matemática para encontrar o N-ésimo número na sequência de Fibonacci também usa recursão

# Crie uma função fib(n) que retorna o n-ésimo número da sequência de Fibonacci.
# %% --begin

def fib(n):
    """
    The function calculates the nth Fibonacci number recursively in Python.
    
    :param n: In the given code snippet, the function `fib(n)` calculates the nth Fibonacci number
    recursively. The function returns the Fibonacci number at position `n`
    :return: The code is calculating the 10th number in the Fibonacci sequence using a recursive
    function. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the
    two preceding numbers.
    """
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return(fib(n-1)+ fib(n-2))

print(fib(10))
# %% --end
