'''Exercício 2 – Classe ContaBancaria
1. Crie uma classe chamada ContaBancaria com:
Atributos: 
titular (string), 
saldo (float).

Métodos:
depositar(valor) → adiciona ao saldo.
sacar(valor) → subtrai do saldo se houver saldo suficiente.
exibir_saldo() → mostra o saldo atual.

2. Crie uma conta para "João" com saldo inicial de 1000.
Deposite 500.
Saque 300.
Exiba o saldo final.'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
            return
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de valor R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")
    
    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: RS{self.saldo:.2f}")

# ---- Testando o programa ----

# 2. Crie uma conta para "João" com saldo inicial de 1000.

conta_joao = ContaBancaria("João", 1000)

# Deposite 500.
conta_joao.depositar(500)

# Saque 300.
conta_joao.sacar(300)

# Mostrar o saldo de João
conta_joao.exibir_saldo()