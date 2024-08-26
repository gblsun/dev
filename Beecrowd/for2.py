# range -> é uma função "PRONTA" em Python
# que determina o número de repetições que 
# meu programa irá realizar

maior_idade = 19
for count in range(5):
    idade = int(input("Digite a idade do aluno: "))
    if idade > maior_idade:
        maior_idade = idade
        print("A maior idade é", maior_idade)