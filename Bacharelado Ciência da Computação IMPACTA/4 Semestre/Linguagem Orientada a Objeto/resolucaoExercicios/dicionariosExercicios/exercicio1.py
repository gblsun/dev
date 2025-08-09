'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
Exercício resolvido dia 08/08/2025.
Exercício 01
 
Preencha um dicionário com as informações de 5 produtos fornecidos pelo usuário. - 
→ Solicite os dados ao usuário 
→ Utilize o nome do produto como chave e o preço como valor. 
→ Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50,00. 

Exemplo: 
Veja um exemplo da estrutura do dicionário. 
{'caneta': 3.0, 'Pen drive': 100.0,'Teclado': 30.0, 'Lápis': 1.5} 
'''
dicionario = {}
for i in range(5):
    produto = input(f"Digite o nome do produto n° {i + 1}: ")
    valor = float(input(f"Digite o valor de seu produto n° {i + 1}: "))
    dicionario[produto] = valor
print(dicionario)

print("\nProdutos com preço superior a R$50,00:")
for produto, valor in dicionario.items():
    if valor >= 50:
        print(f"{produto}: R$ {valor:.2f}")
