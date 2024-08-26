# Exercício de Gabriel Muchon Pavanelli;
# ||Ciência da Computação 1B;

nome = input("Digite seu nome: ")
jedi_favorito = input("Digite seu Jedi favorito: ")
lado_da_forca = input("Digite seu lado da força (Luz/Trevas): ")
resp = input(f"{nome}, você deseja calcular a área do papelão? (S/N): ")

if resp == "S" or resp == "s":
    n1 = int(input("Digite o valor da base da caixa de papelão: "))
    n2 = int(input("Digite o valor da altura da caixa de papelão: "))
    area = n1 * n2

    if lado_da_forca == "Luz" or lado_da_forca == "luz":
        print(f"Olá {nome}, você é do lado da {lado_da_forca}.")
    elif lado_da_forca == "Trevas" or lado_da_forca == "trevas":
        print(f"Olá {nome}, você é do lado das {lado_da_forca}.")
    else:
        print("É necessário escolher um lado da força!")
        
    print(f"Seu Jedi favorito é: {jedi_favorito}")
    print(f"A área da caixa de papelão é: {area}.")
    
else:
    if lado_da_forca == "Luz" or lado_da_forca == "luz":
        print(f"Olá {nome}, você é do lado da {lado_da_forca}.")
    elif lado_da_forca == "Trevas" or lado_da_forca == "trevas":
        print(f"Olá {nome}, você é do lado das {lado_da_forca}.")
    else:
        print("É necessário escolher um lado da força!")
    print(f"Seu Jedi favorito é: {jedi_favorito}")
