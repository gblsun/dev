# Estruturas de repetição em Python
# 1- While : O While caracteriza-se por uma estrura que efetua 
# um TESTE LÓGICO no INÍCIO de um looping
# While -> ENQUANTO -> Condição
# While -> Quando eu NÃO SEI quantas vezes preciso executar 
# o programa
# opc = operation controller

opc = 1
while opc ==1:
    num = int(input("Digite um número:"))
    if num == 0:
        print("É Zero!!!!")
    elif num>0:
        print("É +")
    else:
        print("É -")
    resp = input("Você deseja finalizar? (S/N)")
    if resp == "S" or resp == "s":
        opc = 2
print("Programa Finalizado")
print("Hoje é sexta-feira, dia da maldade")
print("Quero Férias!!!")

