N = int(input("Digite um número (1-10)"))

if N >= 0 and N <=10: 
    for count in range(1, 11):
        print(f"{N} x {count} = {N * count}")
else:
    print("O número deve estar entre 0 e 10")
    
