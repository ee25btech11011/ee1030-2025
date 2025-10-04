import ctypes
import os
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the C library
if os.name == "nt":  # Windows
    lib = ctypes.CDLL("./code11.dll")
else:
    lib = ctypes.CDLL("./code11.so")

from ctypes import c_double

lib.solve_real_p.argtypes = [ctypes.POINTER(c_double)]
lib.solve_real_p.restype = ctypes.c_int

# Array to store real roots
p_real_array = (c_double * 2)()
num_roots = lib.solve_real_p(p_real_array)

# Use the first real root (p = -1)
p = p_real_array[0]
print(f"Real solution from C function: p = {p}")

# Step 2: Define the lines
q = 1  # arbitrary value
x = np.linspace(-5, 5, 400)

# Line equations
y1 = p*(p**2 + 1)*x + q
y2 = -((p**2 + 1)**2 * x + 2*q)/(p**2 + 1)

# Step 3: Common perpendicular
# Slope of perpendicular line: m_perp = 1/2
m_perp = 1 / 2

# Choose a point halfway between the two lines at x=0
y_mid = (y1[200] + y2[200]) / 2
x_perp = np.linspace(-5, 5, 400)
y_perp = m_perp * x_perp + y_mid  # line passing through midpoint

# Step 4: Plot everything
plt.figure(figsize=(7, 5))
plt.plot(x, y1, label='L1: p(p^2+1)x - y + q = 0', color='blue')
plt.plot(x, y2, label='L2: (p^2+1)^2 x + (p^2+1)y + 2q = 0', color='red')
plt.plot(x_perp, y_perp, '--', label='Common perpendicular', color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Lines and Common Perpendicular for p = {p}')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Step 5: Save figure
plt.savefig("fig11.png", dpi=300)
plt.show()
