'''
Exercício 2 – Classe ContaBancaria
1. Crie uma classe chamada ContaBancaria com:
○ Atributos: titular (string), saldo (float).
○ Métodos:
■ depositar(valor) → adiciona ao saldo.
■ sacar(valor) → subtrai do saldo se houver saldo suficiente.
■ exibir_saldo() → mostra o saldo atual.
2. Crie uma conta para &quot;João&quot; com saldo inicial de 1000.
○ Deposite 500.
○ Saque 300.
○ Exiba o saldo final.
'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        