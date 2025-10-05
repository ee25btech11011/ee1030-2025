import numpy as np
import matplotlib.pyplot as plt
import math

# Input: Line equations
# Line 1: 3x - 4y - 7 = 0  →  n1^T x = d1
# Line 2: 2x - 3y - 5 = 0  →  n2^T x = d2
n1 = np.array([3, -4])
n2 = np.array([2, -3])
d1 = 7
d2 = 5

# Area of circle
area = 49 * math.pi
r = math.sqrt(area / math.pi)  # Radius = √(Area/π) = √49 = 7

# Solve for center
# Solve:
# [n1^T] [c] = d1
# [n2^T] [c] = d2

A = np.vstack((n1, n2))
d = np.array([d1, d2])

center = np.linalg.solve(A, d)  # [h, k]
h, k = center

# Compute b and c for general form
# General form: x^2 + y^2 + 2b^T x + c = 0
b = -center
c_val = b @ b - r**2

# Display equation
print("\n--- Circle Parameters ---")
print(f"Center (h, k): ({h:.3f}, {k:.3f})")
print(f"Radius: {r:.3f}")
print(f"General Form: x² + y² + 2({b[0]:.1f})x + 2({b[1]:.1f})y + ({c_val:.1f}) = 0")

# Plotting
theta = np.linspace(0, 2 * np.pi, 400)
x_circle = h + r * np.cos(theta)
y_circle = k + r * np.sin(theta)

x_vals = np.linspace(-10, 10, 400)
y1 = (n1[0] * x_vals - d1) / -n1[1]
y2 = (n2[0] * x_vals - d2) / -n2[1]

plt.figure(figsize=(6, 6))
plt.plot(x_circle, y_circle, 'b', label='Circle')
plt.plot(x_vals, y1, 'r--', label='3x - 4y - 7 = 0')
plt.plot(x_vals, y2, 'g--', label='2x - 3y - 5 = 0')
plt.scatter(h, k, color='black', s=50)
plt.text(h, k, f'  ({h:.0f}, {k:.0f})', fontsize=10, color='black', va='center', ha='left')

plt.title("Circle from Diameter Lines")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.tight_layout()
plt.savefig("circle_plot.png", dpi=300)
plt.show()
