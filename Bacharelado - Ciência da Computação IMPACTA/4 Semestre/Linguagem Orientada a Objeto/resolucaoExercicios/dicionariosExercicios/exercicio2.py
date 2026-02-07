'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
Exercício 02 

Preencha um dicionário com os dados de 5 alunos fornecidos pelo usuário.
→ Solicite os dados do usuário
→ Utilize o ra do aluno como chave e uma lista de três notas como valor. 
→ Percorra o dicionário e exiba a média de cada aluno. 

Exemplo: 

Veja um exemplo da estrutura do dicionário. 
{19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]} '''

dicionario = {}
for i in range(5):
    ra = input(f"Digite o RA n° {i + 1}: ")
    nota = []
    for cont in range(3):
        n = float(input(f"Digite a nota n° {cont + 1}: "))
        nota.append(n)
    dicionario[ra] = nota
print(dicionario)

print("\nMédias dos alunos:")
for ra, notas in dicionario.items():
    media = sum(notas) / len(notas)
    print(f"RA {ra}: média = {media:.2f}")