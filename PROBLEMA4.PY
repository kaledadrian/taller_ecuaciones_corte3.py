import numpy as np
import matplotlib.pyplot as plt

# Intervalo
t = np.linspace(0, 10, 1000)

# Solución general
x = (
    np.cos(2*t)
    + np.sin(2*t)
    + t*np.cos(2*t)
    + t*np.sin(2*t)
)

# Gráfica
plt.plot(t, x)

plt.title("Problema 4 - Redes y Buffer")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)

plt.show()