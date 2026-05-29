import numpy as np
import matplotlib.pyplot as plt

# Intervalo
t = np.linspace(0, 10, 1000)

# Solución general
z = (
    np.exp(-t)
    + t*np.exp(-t)
    + t**2*np.exp(-t)
    + (1/6)*t**3*np.exp(-t)
)

# Gráfica
plt.plot(t, z)

plt.title("Problema 5 - Control de Altitud Drone")
plt.xlabel("t")
plt.ylabel("z(t)")
plt.grid(True)

plt.show()