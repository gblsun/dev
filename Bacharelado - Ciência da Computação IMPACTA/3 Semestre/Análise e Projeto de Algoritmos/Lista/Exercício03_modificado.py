# não consegui desenvolver.

from datetime import datetime

# Obter a data atual
# data_atual = datetime.now
# mes_atual = data_atual.strftime("%B") #n Nome do mês por extenso
# mes_atual = data_atual.strftime("%B") if isinstance(data_atual, datetime) else "Mês desconhecido"

nome = input("Nome do funcionário: ")
salario = float(input("Salário: "))
print(f"O funcionário {nome} tem um salário de R${salario:.2f} em {mes_atual}.")
