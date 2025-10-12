import numpy as np
import matplotlib.pyplot as plt

# Quadratic coefficients
a = 6
b = -1
c = -2

# Compute discriminant
discriminant = b**2 - 4*a*c

# Compute roots
if discriminant >= 0:
    x1 = (-b + np.sqrt(discriminant)) / (2*a)
    x2 = (-b - np.sqrt(discriminant)) / (2*a)
else:
    x1 = x2 = np.nan  # complex roots

print("Roots:", x1, x2)

# Plot the quadratic
x = np.linspace(min(x1, x2) - 1, max(x1, x2) + 1, 400)
y = a*x**2 + b*x + c

plt.figure(figsize=(8,6))
plt.plot(x, y, label=f'$y = {a}x^2 {b:+}x {c:+}$\nRoots: x1={x1:.2f}, x2={x2:.2f}')
plt.axhline(0, color='black', linewidth=1)
plt.scatter([x1, x2], [0,0], color='red', zorder=5)

# Label the roots above the curve
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
