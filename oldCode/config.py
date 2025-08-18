import numpy as np

#constant
PI = np.pi

# Schwarzschild radius
r_s = 2  

# Create grid of radius and theta
r = np.linspace(r_s, 10, 100)
theta = np.linspace(0, 2*np.pi, 120)
R, T = np.meshgrid(r, theta)

# Convert polar to Cartesian
X = R * np.cos(T)
Y = R * np.sin(T)

# Embedding height function ± 2 sqrt(r_s * (r - r_s))
Z_pos = 2 * np.sqrt(r_s * (R - r_s))
Z_neg = - Z_pos