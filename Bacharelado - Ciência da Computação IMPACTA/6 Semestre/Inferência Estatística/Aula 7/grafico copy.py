import matplotlib.pyplot as plt
import numpy as np

# Passo 3: Dados da tabela (X: Quantis Teóricos Z, Y: Valores Observados)
x = [-1.18, -0.50, 0.00, 0.50, 1.18]
y = [10, 12, 14, 15, 18]

# Ajuste da reta de tendência que passa pelo ponto central (Z_medio=0, x_medio=13.8)
slope, intercept = np.polyfit(x, y, 1)

# Intervalo do eixo X conforme instruído (-1.5 a +1.5)
x_reta = np.array([-1.5, 1.5])
y_reta = slope * x_reta + intercept

plt.figure(figsize=(7, 5))

# Plot dos 5 pontos observados
plt.scatter(x, y, color='blue', zorder=5, label='Pontos Observados')

# Plot da reta de referência
plt.plot(x_reta, y_reta, color='red', linestyle='--', label='Reta de Tendência')

# Destaque do ponto central (0; 13,8)
plt.scatter([0], [intercept], color='red', s=60, zorder=6, label='Ponto Central (0; 13,8)')

# Configuração dos limites e rótulos dos eixos (Passo 4)
plt.xlim(-1.5, 1.5)
plt.ylim(9, 19)

plt.title('Q-Q Plot: Análise de Normalidade')
plt.xlabel('Quantis Teóricos de Normal Padrão ($Z$)')
plt.ylabel('Valores Observados ($x$)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')

plt.show()