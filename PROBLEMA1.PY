import numpy as np
import matplotlib.pyplot as plt

# Intervalo de tiempo
t = np.linspace(0, 10, 500)

# Solución de la ecuación diferencial
v = np.exp(-t) + np.exp(-t/2) * (
    np.cos((np.sqrt(3)/2)*t) +
    np.sin((np.sqrt(3)/2)*t)
)

# Gráfica
plt.plot(t, v)
plt.title("Problema 1 - Filtro Pasabajas")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.grid(True)

plt.show()