import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from config import *

# flat event horizon disk
def make_horizon(z_center):
    pass

# Black-hole 
def make_blackhole(center_z):
    phi = np.linspace(0, PI, 30)
    theta_s = np.linspace(0, 2*PI, 30)
    PHI, THETA_S = np.meshgrid(phi, theta_s)
    Xs = r_s * np.sin(PHI) * np.cos(THETA_S)
    Ys = r_s * np.sin(PHI) * np.sin(THETA_S)
    Zs = r_s * np.cos(PHI) + center_z
    return Xs, Ys, Zs

#top black hole
Xs_top, Ys_top, Zs_top = make_blackhole(Z_pos.max())
Xs_bottom, Ys_bottom, Zs_bottom = make_blackhole(Z_neg.max())

# Setup figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot both sheets (wormhole)
wire1 = ax.plot_wireframe(X, Y, Z_pos, color='cyan', linewidth=0.5)
wire2 = ax.plot_wireframe(X, Y, Z_neg, color='cyan', linewidth=0.5)

# Black holes at top and bottom
blackhole_top = ax.plot_surface(Xs_top, Ys_top, Zs_top, color='black', shade=True)
blackhole_bottom = ax.plot_surface(Xs_bottom, Ys_bottom, Zs_bottom, color='black', shade=True)


# Style
ax.set_facecolor('black')
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_box_aspect([1, 1, 1])

# FPS tracking variables
frame_count = 0
last_time = time.perf_counter()
fps_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, color='white')

# Animation update function
def update(frame):
    global frame_count, last_time
    ax.view_init(elev=30, azim=frame)  # rotate view
    
    frame_count += 1
    current_time = time.perf_counter()
    elapsed = current_time - last_time
    
    # Update FPS every 10 frames for stability
    if frame_count % 10 == 0:
        fps = frame_count / elapsed
        fps_text.set_text(f"FPS: {fps:.2f}")
        frame_count = 0
        last_time = current_time
    
    return wire1, wire2, fps_text

# Run animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=30, blit=False, repeat=True)

plt.show()
