"""Projectile trajectory gallery example.

This example computes and plots the flight paths of a projectile launched
at six different angles with the same initial speed, neglecting air resistance.
Each trajectory is generated using simple kinematic equations in NumPy.
"""

import matplotlib.pyplot as plt
import numpy as np

v0 = 20.0  # initial speed in m/s
angles = np.deg2rad([15, 30, 45, 60, 75, 85])
g = 9.8

fig, ax = plt.subplots(figsize=(10, 6))
for angle in angles:
    T = 2 * v0 * np.sin(angle) / g
    t = np.linspace(0, T, 200)
    x = v0 * np.cos(angle) * t
    y = v0 * np.sin(angle) * t - 0.5 * g * t**2
    ax.plot(x, y, label=f"{np.rad2deg(angle):.0f}°")

ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("Range (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile Trajectories at Different Launch Angles")
ax.legend(title="Launch angle")
ax.grid(True, linestyle="--", alpha=0.5)

plt.show()