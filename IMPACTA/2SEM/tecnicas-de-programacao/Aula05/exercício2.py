# %%
# imports

import random

# Funções

def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])

def gerar_subconjunto(conjunto):
    return set(random.sample(list(conjunto), int(random.random() * 100)))

conjunto_pessoas = set ()
for i in range(100):
    gerar_cpf()
    conjunto_pessoas.add(gerar_cpf())
    print(conjunto_pessoas)


# %%
# Definir conjunto vazio
#
