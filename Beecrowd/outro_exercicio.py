def coletar_notas():
    numero_de_notas = int(input())
    lista_de_notas = []

    for _ in range(numero_de_notas):
        lista_de_notas.append(float(input()))

    return lista_de_notas

def calcular_notas_finais(notas_originais, notas_para_alterar):
    total_notas_alteradas = 0

    for indice in range(len(notas_originais)):
        if (notas_para_alterar[indice] == 10 and notas_originais[indice] < 10):
            notas_para_alterar[indice] = min(notas_originais[indice] + 2, 10)
            total_notas_alteradas += 1
        else:
            notas_para_alterar[indice] = notas_originais[indice]

    return total_notas_alteradas

def exibir_notas_alteradas(notas_originais, notas_finais, total_notas_alteradas):
    print(f'NOTAS ALTERADAS: {total_notas_alteradas}')
    for indice in range(len(notas_originais)):
        simbolo_nota_alterada = ('*' if notas_originais[indice] != notas_finais[indice] else '-')
        posicao_nota = f'({indice+1:03})'
        nota_original_formatada = f'{notas_originais[indice]:05.2f}'
        nota_final_formatada = f'{notas_finais[indice]:05.2f}'
        print(f'{simbolo_nota_alterada}{posicao_nota} original: {nota_original_formatada} | final: {nota_final_formatada}')

def main():
    notas_iniciais = coletar_notas()
    notas_para_alterar = coletar_notas()
    total_notas_alteradas = calcular_notas_finais(notas_iniciais, notas_para_alterar)
    exibir_notas_alteradas(notas_iniciais, notas_para_alterar, total_notas_alteradas)

if __name__ == "__main__":
    main()
