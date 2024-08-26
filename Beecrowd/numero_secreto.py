numero_secreto = 8
tentativas = 0

print("Bem vindo(a) ao jogo da adivinhação")
print("Adivinhe o número secreto. (1-20)")
while True:
    tentativa = int(input("Digite um número:"))
    tentativas = tentativas+1
    
    if tentativa == numero_secreto:
        print("Você é o/a cara/mina!!. Você advinhou em:",tentativas,"tentativas")
        break
    elif tentativa < numero_secreto:
        print("Tente um numero maior")
    else:
        print("Tente um numero menor")