'''
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
|                                                                                      |
| Exercícios: Linguagem Orientada a objetos IMPACTA 08 de Agosto de 2025               |
| Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)        |
|                                                                                      |
<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+<--x-->+
Exercício resolvido dia 08/08/2025.

Suponha que você foi contratado para desenvolver uma funcionalidade no sistema do RH de um novo banco digital. Esse banco teve acesso ao cadastro de clientes de outras três empresas concorrentes (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais clientes. Para isso, pediu que você gerasse um relatório com 12 items. Atenção, use apenas um print por item.
'''

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

# 01) Quais são os clientes de cada uma, separadamente.
print("Clientes de cada uma, separadamente.\nNubank: " ,nubank,"\nC6: " ,c6, "\nInter: ",inter)

# 02) Quais são os clientes de todas as concorrentes.
print("\nClientes de todas as concorrentes: ", nubank , c6 , inter)

# 03) Quais são os clientes da Nubank que também são clientes do C6.
print("Clientes da Nubank que também são clientes do C6: ", nubank.intersection(c6))
    
# 04) Quais são os clientes da Nubank que também são clientes do Inter.
print("Clientes da Nubank que também são clientes do Inter: ", nubank.intersection(inter))

# 05) Quais são os clientes do C6 que também são clientes do Inter.
print("Clientes do C6 que também são clientes do Inter: ", c6.intersection(inter))

# 06) Quais são os clientes apenas da Nubank.
print("Clientes apenas da Nubank: ", (nubank - (c6 | inter)))

# 07) Quais são os clientes apenas do C6.
print("Clientes apenas da C6: ", (c6 - (nubank | inter)))

# 08) Quais são os clientes apenas do Inter.
print("Clientes apenas da Inter: ", (inter - (nubank | c6)))

# 09) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.
print("Clientes da Nubank e C6, mas não das duas ao mesmo tempo: ", (nubank.symmetric_difference(c6)))


# 10) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.
print("Clientes da Nubank e Inter, mas não das duas ao mesmo tempo: ", (nubank.symmetric_difference(inter)))


# 11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.
print("Clientes da C6 e Inter, mas não das duas ao mesmo tempo: ", (c6.symmetric_difference(inter)))

# 12) Quais são os clientes das três simultaneamente.
print("Clientes da C6 e Inter, mas não das duas ao mesmo tempo: ", (nubank & c6 & inter))
