
# 1. Determinar se um ano fornecido pelo usuário é bissexto ou não.
ano = int(input("Digite um ano: "))
if (ano % 4 == 0) or (( ano % 100 == 0 ) and (ano % 400 == 0)):
    print("O ano:", ano ," digitado é Bissexto. ")
else:
    print("O ano digitado não é Bissexto. ")

