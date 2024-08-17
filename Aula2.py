# %% Produto de Matrizes em Python

import numpy as np
import pandas as pd

A = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])
prod = A.dot(B)

df_A = pd.DataFrame(A)
df_B = pd.DataFrame(B)
df_prod = pd.DataFrame(prod)

print(f"O produto de \n\n{df_A}\n\nvezes\n\n{df_B}\n\né igual à:\n\n{df_prod}")

# %% Cálculo de determinante no Python

import numpy as np
import pandas as pd

A2 = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])
B2 = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])
determinante = np.linalg.det(B2)

df_A2 = pd.DataFrame(A2)
df_B2 = pd.DataFrame(B2)

print(f"A determinante de\n\n{df_B2}\n\né\n\n{determinante}")
print(determinante)
print(
    f"\n\nOu preferes assim:\n\nA determinante de\n\n{B2}\n\né\n\n{determinante}\n\n(Desta forma é sem utilizar a biblioteca pandas)"
)

# %% Produto de Matrizes em Python
import numpy as np

A = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])
prod = A.dot(B)
print(prod)
# %%
