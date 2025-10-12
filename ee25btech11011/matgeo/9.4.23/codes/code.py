import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared C library
lib = ctypes.CDLL("./code15.so")  # or .dll on Windows

# Prepare C function
lib.roots.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.roots.restype = None

# Create C doubles to store the roots
root1 = ctypes.c_double()
root2 = ctypes.c_double()

# Call C function
lib.roots(ctypes.byref(root1), ctypes.byref(root2))

# Extract Python values
x1 = root1.value
x2 = root2.value

print("Roots from C:", x1, x2)

# Plot the quadratic
x = np.linspace(min(x1, x2) - 1, max(x1, x2) + 1, 400)
y = 6*x**2 - x - 2

plt.figure(figsize=(8,6))
# Include the roots in the legend label
plt.plot(x, y, label=f'$y = 6x^2 - x - 2$\nRoots: x1={x1:.2f}, x2={x2:.2f}')
plt.axhline(0, color='black', linewidth=1)
plt.scatter([x1, x2], [0,0], color='red', zorder=5)

# Label the roots on the graph (optional)
offset_y = max(y)*0.05
offset_x = 0.02
plt.text(x1 + offset_x, 0 + offset_y, f'x1({x1:.2f})', ha='left', va='bottom', color='red')
plt.text(x2 + offset_x, 0 + offset_y, f'x2({x2:.2f})', ha='left', va='bottom', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphical solution of 6x^2 - x - 2 = 0')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig('fig15.png', dpi=300)
plt.show()
