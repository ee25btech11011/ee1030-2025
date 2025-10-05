import ctypes
import os
import math
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled C library
if os.name == "nt":   # Windows
    lib = ctypes.CDLL("./code13.dll")
else:
    lib = ctypes.CDLL("./code13.so")

# Define argument and return types for C function
lib.solve_circle.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.solve_circle.restype = None

# Input values (example from question)
# Lines: 3x - 4y - 7 = 0  and  2x - 3y - 5 = 0
# Area = 49π
a1, b1, c1 = 3, -4, -7
a2, b2, c2 = 2, -3, -5
area = 49 * math.pi

# Prepare array of doubles (13 elements)
params = (ctypes.c_double * 13)()
params[0] = a1
params[1] = b1
params[2] = c1
params[3] = a2
params[4] = b2
params[5] = c2
params[6] = area

# Call the C function
lib.solve_circle(params)

# Retrieve results
h, k, r, D, E, F = params[7], params[8], params[9], params[10], params[11], params[12]

# Print results
print("\n--- Circle Parameters ---")
print(f"Center (h, k): ({h:.3f}, {k:.3f})")
print(f"Radius: {r:.3f}")
print(f"Equation: x^2 + y^2 {D:+.3f}x {E:+.3f}y {F:+.3f} = 0")

# Plot circle and diameter lines
theta = np.linspace(0, 2 * np.pi, 400)
x_circle = h + r * np.cos(theta)
y_circle = k + r * np.sin(theta)

# Lines
x_vals = np.linspace(-10, 10, 300)
y1 = (a1 * x_vals + c1) / (-b1)
y2 = (a2 * x_vals + c2) / (-b2)

plt.figure(figsize=(6, 6))
plt.plot(x_circle, y_circle, 'b', label='Circle')
plt.plot(x_vals, y1, 'r--', label=f'{a1}x {b1:+}y {c1:+} = 0')
plt.plot(x_vals, y2, 'g--', label=f'{a2}x {b2:+}y {c2:+} = 0')
plt.scatter(h, k, color='black', s=50, label='Center (1,-1)')
plt.text(h, k, '  (1, -1)', fontsize=10, color='black', va='center', ha='left')
plt.title("Circle with Given Diameter Lines")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.axis('equal')

# Save figure as fig13.png
plt.savefig("fig13.png", dpi=300)

# Show the figure
plt.show()
