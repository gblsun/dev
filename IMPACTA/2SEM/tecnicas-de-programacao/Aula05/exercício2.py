# %% --begin
import random

# Declaração de função
def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])

def gerar_subconjunto(conjunto):
    return set(random.sample(list(conjunto), int(random.random() * 100)))

# Conjunto nulo
conjunto_pessoas = set()

# Loop do programa
while len(conjunto_pessoas) < 100:
    cpf = gerar_cpf()
    conjunto_pessoas.add(cpf)

# Declaração dos subconjuntos
esportes = {
    "surfe": gerar_subconjunto(conjunto_pessoas),
    "volei": gerar_subconjunto(conjunto_pessoas),
    "ginastica": gerar_subconjunto(conjunto_pessoas),
    "judo": gerar_subconjunto(conjunto_pessoas),
}
# Calcule a probabilidade de que uma pessoa sorteada aleatoriamente tenha assistido:
# Judô ou surfe
# Pelo menos dois esportes
# Todos os esportes
# Nenhum esporte

uniao_judo_surfe = esportes["judo"] | esportes["surfe"]
print(len(uniao_judo_surfe))
# %% --end