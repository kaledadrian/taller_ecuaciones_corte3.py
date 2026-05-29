import numpy as np
import matplotlib.pyplot as plt

# Intervalo
t = np.linspace(0, 6, 500)

# Solución exacta
theta = (4/9) - (4/9)*np.exp(-3*t) - (4/3)*t*np.exp(-3*t)

# Gráfica
plt.plot(t, theta)

plt.title("Problema 2 - Brazo Robotico")
plt.xlabel("t")
plt.ylabel("Theta(t)")
plt.grid(True)

plt.show()