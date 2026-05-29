import numpy as np
import matplotlib.pyplot as plt

# Intervalo
t = np.linspace(0, 4, 500)

# Solución general
T = np.exp(2*t) + t*np.exp(2*t) + np.exp(-t) + 3

# Gráfica
plt.plot(t, T)

plt.title("Problema 3 - Temperatura Data Center")
plt.xlabel("t")
plt.ylabel("T(t)")
plt.grid(True)

plt.show()
