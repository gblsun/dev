notaTrabalho = float(input("trabalho"))
notaProva = float(input("prova"))
media = (notaTrabalho + notaProva)/2

if media >= 6.00:
    print("aprovado")
else:
    if (notaTrabalho + 10)/2 >= 6:
        print("talvez com a sub")
    else:
        print("reprovado")
