vendas = int(input('Digite a quantidade de vendas: '))

if vendas > 500:
    bonus = 50
else:
    bonus = 0

print('O bonus é:', bonus)


vendas = int(input('Digite a quantidade de vendas: '))

bonus = 50 if vendas > 500 else 0
#<expressão1> if <condição> else <expressão2>

print('O bonus é:', bonus)

#do while
while True:
    #instruções
    if <cond>:
        break
