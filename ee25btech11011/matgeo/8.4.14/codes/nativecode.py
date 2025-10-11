import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a_ellipse = 2.0   # semi-major axis
b_ellipse = 1.0   # semi-minor axis

# Eccentricity and focus distance
e = np.sqrt(1 - (b_ellipse**2) / (a_ellipse**2))
c = a_ellipse * e

# Latus rectum endpoints (y < 0)
xP, yP = c, -0.5
xQ, yQ = -c, -0.5

# Midpoint (vertex) V of latus rectum
xV = (xP + xQ) / 2
yV = (yP + yQ) / 2

# Parabola parameters
lengthPQ = np.sqrt((xP - xQ)**2 + (yP - yQ)**2)
a_p = lengthPQ / 4

# Coefficient 2 * sqrt(3)
coeff = 2 * np.sqrt(3)
constant = -coeff * yV

print(f"Parabola equation: x^2 - 2√3 y = {constant:.4f}")

# Prepare plot
theta = np.linspace(0, 2*np.pi, 400)
x_ellipse = a_ellipse * np.cos(theta)
y_ellipse = b_ellipse * np.sin(theta)

# Parabola: x^2 = 2√3 (y + 0.5) -> y = x^2 / (2√3) - 0.5
x_parabola = np.linspace(-4, 4, 400)
y_parabola = (x_parabola**2) / (2 * np.sqrt(3)) - 0.5

plt.figure(figsize=(8, 6))
plt.plot(x_ellipse, y_ellipse, label='Ellipse: $x^2 + 4y^2 = 4$', color='blue', linewidth=2)
plt.plot(x_parabola, y_parabola, label='Parabola', color='red', linewidth=2)

# Mark latus rectum endpoints and vertex
plt.scatter([xP, xQ], [yP, yQ], color='green', s=60, zorder=5, label='Endpoints P, Q')
plt.scatter(xV, yV, color='purple', s=60, zorder=5, label='Vertex V')

# Label points
plt.text(xP, yP, 'P', fontsize=12, ha='right', va='top')
plt.text(xQ, yQ, 'Q', fontsize=12, ha='left', va='top')
plt.text(xV, yV, 'V', fontsize=12, ha='center', va='bottom')

# Axes and grid
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Ellipse and Parabola with Latus Rectum', fontsize=14)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Save figure
plt.savefig('fig14.png', dpi=300)
plt.show()
