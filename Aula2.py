# %% Produto de Matrizes em Python

import numpy as np
import pandas as pd

A=np.array([[1,-3,4],[3,6,9],[-1,5,4]])
B=np.array([[3,4,-1],[5,-1,5],[4,6,5]])
prod=A.dot(B)

df_A = pd.DataFrame(A)
df_B = pd.DataFrame(B)
df_prod = pd.DataFrame(prod)

print(f"O produto de \n\n{df_A}\n\nx\n\n{df_B}\n\né igual à:\n\n{df_prod}")

# %%