'''

30/03/2025 - atividade avaliativa de Análise e Projeto de Algoritmos

Orientações:
Apenas as funções estas funções podem ser usadas nas implementações; 
→range()
→len()
→.append()
Demais funções e bibliotecas do Python estão proibidas;
<--------->|<--------->|<--------->|<--------->|<--------->|<--------->|<--------->|<--------->

Execute as células com os casos de teste propostos para cada uma das funções desenvolvidas.
Implemente uma solução para os seguintes problemas:

Transporte de pedras: Tomando N pedras onde cada uma tem peso 1kg maior que a anterior 
(pedra1=1kg, pedra2=2kg, pedra3=3kg, ..., pedraN=Nkg), 
determine a forma de transportá-las em um veículo com capacidade máxima de C (kg) por vez com o mínimo de deslocamentos.
A solução para este problema deve ser implementada com a estratégia gulosa.
Corte de toras:Considere uma tora de madeira de comprimento L (m), a qual desejamos cortá-la N vezes em posições determinadas pela lista [p1,p2,p3,...,pN]. Cada corte custa R reais por metro de tora a ser cortada, por exemplo se R=5 e L=10, o valor será R$ 50,00 independente do ponto de corte. Determine o valor total mínimo para os N cortes.

A solução para este problema deve ser implementada com a estratégia de programação dinâmica.
'''

def transporte_pedras(N, C):
    # -------> essa parte serve para criar a quantidade de pedras
    pedras = []
    for i in range(1, N + 1):
        pedras.append(i)  # append serve para adicionar o valor no final da lista

    viagens = 0  # No início, nenhuma viagem foi feita, então o contador começa em 0.

    while len(pedras) > 0:  # Enquanto houver pedras para transportar
        carga_atual = 0  # Peso da carga atual
        nova_lista = []  # Lista para armazenar as pedras que não couberam na viagem atual

        for i in range(len(pedras)):  # Percorre a lista de pedras
            if carga_atual + pedras[i] <= C:  # Se a pedra couber na carga
                carga_atual += pedras[i]  # Adiciona o peso da pedra à carga
            else:
                nova_lista.append(pedras[i])  # Se não couber, coloca a pedra de volta na nova lista para a próxima viagem
        
        pedras = nova_lista  # Atualiza a lista de pedras para as que não foram transportadas
        viagens += 1  # Incrementa o número de viagens
    
    return viagens  # Retorna o número total de viagens

def corte_toras(L, cortes, R):
    # -------> Adiciona o comprimento total da tora no final da lista de cortes
    cortes.append(L)
    custo_total = 0  # Inicializa o custo total
    ''' 
    → L é o comprimento total da tora da madeira.
    → cortes é uma lista que contém as posições onde a tora deve ser cortada.
    → R é o custo por metro.
    '''
    while len(cortes) > 2:  # Enquanto houver mais de 2 cortes
        min_custo = 9999999999  # Inicializa o custo mínimo como um valor muito alto, ou seja: simula o infinito
        min_index = -1  # Inicializa o índice do corte de menor custo

        # Percorre os cortes possíveis
        for i in range(1, len(cortes) - 1):
            custo = (cortes[i + 1] - cortes[i - 1]) * R  # Calcula o custo do corte
            if custo < min_custo:  # Se o custo for menor que o custo mínimo atual
                min_custo = custo  # Atualiza o custo mínimo
                min_index = i  # Atualiza o índice do corte de menor custo

        custo_total += min_custo  # Adiciona o custo mínimo ao custo total
        
        nova_lista = []  # Nova lista de cortes sem o corte escolhido
        for i in range(len(cortes)):
            if i != min_index:  # Se não for o corte de menor custo, adiciona à nova lista
                nova_lista.append(cortes[i])
        
        cortes = nova_lista  # Atualiza a lista de cortes
    
    return custo_total  # Retorna o custo total

# Exemplo de uso:
N = 5  # Número de pedras
C = 7  # Capacidade do veículo
print("Mínimo de viagens para transporte:", transporte_pedras(N, C))

L = 10  # Comprimento da tora
cortes = [2, 4, 7]  # Posições dos cortes
R = 5  # Custo por metro
print("Custo mínimo para cortar a tora:", corte_toras(L, cortes, R))
