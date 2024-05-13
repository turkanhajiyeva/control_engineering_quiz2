import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 15, 0.01)

G = cn.ss([[0, 1, 0], [0, 0, 1], [1, -5, -3]], [[0], [0], [1]], [1, 0, 0], [0])

cn.pzmap(G)
plt.title("Pole-Zero Map of G")
plt.figure()
A = np.array([[0, 1, 0], [0, 0, 1], [1, -5, -3]])
K = np.array([[34, 14, 6]])
B = np.array([[0], [0], [1]])

Anew = A - B@K
Gnew = cn.ss(Anew, [[0], [0], [1]], [1, 0, 0], [0])

cn.pzmap(Gnew)
plt.title("Pole-Zero Map of Gnew")
plt.figure()
print(cn.zpk2tf([], [-1+2j, -1-2j, -7], 1))

y, T = cn.step(Gnew, t)
plt.plot(t, y)
plt.title("Step Response of Gnew")
plt.figure()
y, T = cn.step(G, t)
plt.plot(t, y)
plt.title("Step Response of G")

plt.show()
