import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Parameters
grid_size = 50
scale = 0.1
warp_constant = 10.0  # Adjust for warp strength (approximates -M/r)

# Generate grid points
x = np.arange(-grid_size, grid_size + 1) * scale
y = np.arange(-grid_size, grid_size + 1) * scale
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = -warp_constant / np.maximum(r, 0.1)  # Avoid division by zero

# Create the plot
fig = plt.figure(figsize=(10, 7.5))
ax = fig.add_subplot(111, projection='3d')

# Plot the warped grid with color gradient
norm = plt.Normalize(z.min(), z.max())
colors = cm.viridis(norm(z))
ax.plot_wireframe(x, y, z, color='red', linewidth=0.5)

# Add a visible black hole as a red sphere
u = np.linspace(0, 2 * np.pi, 20)
v = np.linspace(0, np.pi, 20)
black_hole_x = 0.1 * np.outer(np.cos(u), np.sin(v))
black_hole_y = 0.1 * np.outer(np.sin(u), np.sin(v))
black_hole_z = 0.1 * np.outer(np.ones(np.size(u)), np.cos(v)) - warp_constant / 0.1
ax.plot_surface(black_hole_x, black_hole_y, black_hole_z, color='red', alpha=0.8)

# Set labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Spacetime Curvature Around a Black Hole')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-15, 5)

# Adjust view angle
ax.view_init(elev=20, azim=45)

# Show the plot
plt.show()