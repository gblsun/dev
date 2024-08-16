

# %% Transposta de Matriz no Python



# Importa as bibliotecas numpy e pandas
import numpy as np
import pandas as pd

# Define a matriz B como um array 2D do numpy
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])

df_B = pd.DataFrame(B)
print(f'A transporta de \n ',df_B ,'\n \né: \n ',df_Bt)

# Calcula a transposta da matriz B
# A transposta de uma matriz é obtida trocando suas linhas por colunas
Bt = np.transpose(B)

# Converte a matriz transposta Bt para um DataFrame do pandas
# Isso facilita a formatação e visualização da matriz transposta
df_Bt = pd.DataFrame(Bt)

# Imprime o DataFrame df_Bt, exibindo a matriz transposta de forma tabular e formatada
print(df_Bt)


# -----------------------------------// Transposta de Matriz no Python
# %% Soma de matrizes com Python


import numpy as np
import pandas as pd

# Define a matriz A como um array 2D do numpy
A = np.array([[1, -3, 4], [3, 6, 9], [-1, 5, 4]])

# Define a matriz B como um array 2D do numpy
B = np.array([[3, 4, -1], [5, -1, 5], [4, 6, 5]])

# Calcula a soma das matrizes A e B
# A soma é realizada elemento a elemento e o resultado é armazenado na matriz C
C = A + B

# Converte o array numpy C para um DataFrame do pandas
# Isso facilita a formatação e visualização da matriz
df_C = pd.DataFrame(C)

# Imprime o DataFrame df_C, exibindo a matriz soma de forma tabular e formatada
print(df_C)

# %% --------------------- Soma de matrizes com Python
