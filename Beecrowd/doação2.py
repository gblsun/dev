total_cripto_vic = 0
vic_coin = float(input())

while vic_coin != -1.0:
    total_cripto_vic+=vic_coin
    vic_coin = float(input())

total_reais = total_cripto_vic * 2.50
print(f'VC$ {total_cripto_vic:.2f}') 
print(f'R$ {total_reais:.2f}')