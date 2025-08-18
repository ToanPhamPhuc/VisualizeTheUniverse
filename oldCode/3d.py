import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(-4 * np.pi, 4 * np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t
ax.plot(x, y, z)
plt.show()