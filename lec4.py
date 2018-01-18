import matplotlib.pyplot as plt
import numpy as np

NN = 20
MU = 2
fig, ax = plt.subplots()
XX = np.linspace(-1, 4, NN)#standard normal dist
YY = XX + np.random.randn(1, NN)
ax.scatter(XX, YY)

plt.show()
