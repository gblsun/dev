# %% --begin
import random


def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])


def gerar_subconjunto(conjunto):
    return set(random.sample(list(conjunto), int(random.random() * 100)))


conjunto_pessoas = set()

while len(conjunto_pessoas) < 100:
    cpf = gerar_cpf()
    conjunto_pessoas.add(cpf)

esportes = {
    "surfe": gerar_subconjunto(conjunto_pessoas),
    "volei": gerar_subconjunto(conjunto_pessoas),
    "ginastica": gerar_subconjunto(conjunto_pessoas),
    "judo": gerar_subconjunto(conjunto_pessoas),
}

# %% --end