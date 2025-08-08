# 4. Gerar a sequência de Fibonacci até um número fornecido pelo usuário
n = int(input("Digite um valor para calcular Fibonacci: "))

sequenciaFibonacci = {}

if n == 0:
    sequenciaFibonacci[0] = 0
    print("O resultado é: ", sequenciaFibonacci[0])

elif n == 1:
    sequenciaFibonacci[0] = 0
    sequenciaFibonacci[1] = 1
    print("O resultado é: ", sequenciaFibonacci[1])

else:
    sequenciaFibonacci[0] = 0
    sequenciaFibonacci[1] = 1

    f1 = sequenciaFibonacci[0]
    f2 = sequenciaFibonacci[1]

    print(f1)
    print(f2)

    for i in range(2, n):
        fib = f1 + f2
        sequenciaFibonacci[i] = fib
        f1 = f2
        f2 = fib

print("Sequência Fibonacci:", ", ".join(str(sequenciaFibonacci[i]) for i in range(n)))


