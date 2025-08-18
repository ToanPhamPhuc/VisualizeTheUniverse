import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Funnel-like Z surface
Z = -1 / np.sqrt(X**2 + Y**2 + 1)  # Avoid division by zero

# Plot figure
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Spacetime Curvature Around a Black Hole")

# Funnel surface
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)

# ===== Black hole sphere at top of funnel =====
# Find Z value at the center (0,0) of funnel
z_center_top = Z[np.argmin(np.abs(x)), np.argmin(np.abs(y))]

# Raise it up a little above the rim for visibility
z_center_top += 0.05  # adjust if needed

# Sphere parameters
r = 0.2
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
xs = r * np.outer(np.cos(u), np.sin(v))
ys = r * np.outer(np.sin(u), np.sin(v))
zs = r * np.outer(np.ones(np.size(u)), np.cos(v))

# Height where the sphere should sit — take max Z at (0,0) + offset
sphere_z_pos = Z[Z.shape[0]//2, Z.shape[1]//2] + 0.1  # 0.1 to make it float above the rim

# Plot sphere
ax.plot_surface(xs, ys, zs + sphere_z_pos, color='black')


# Axes labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
