import numpy as np

import matplotlib.pyplot as plt

import control.matlab as cn


t = np.arange(0, 15, 0.01)

G = cn.ss([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-3, -6, -5, 2]], [[0], [0], [0], [1]], [1, 0, 0, 0], [0])

# cn.rlocus(G)

cn.pzmap(G)

A = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-3, -6, -5, 2]])

K = np.array([[207, 143, 68, 17]])

B = np.array([[0], [0], [0], [1]])

Anew = A - B@K

Gnew = cn.ss(Anew, [[0], [0], [0], [1]], [1, 0, 0, 0], [0])

plt.figure()

cn.pzmap(Gnew)
plt.figure()
# cn.rlocus(G)

print(cn.zpk2tf([], [-1+2j, -1-2j, -6, -7], 1))

y, T = cn.step(Gnew, t)
plt.plot(t, y)
plt.figure()
y, T = cn.step(G, t)
plt.plot(t, y)
# plt.figure()

plt.show()
