import ctypes
import numpy as np
import matplotlib.pyplot as plt

libm = ctypes.CDLL('code14.dll')
libm.sqrt.argtypes = [ctypes.c_double]
libm.sqrt.restype = ctypes.c_double

def c_sqrt(x):
    return libm.sqrt(x)

# Ellipse parameters
a_ellipse = 2.0
b_ellipse = 1.0

# Calculate eccentricity e = sqrt(1 - (b^2)/(a^2))
e = c_sqrt(1 - (b_ellipse**2) / (a_ellipse**2))

# Focus distance c = a * e
c = a_ellipse * e

# Latus rectum endpoints (y < 0)
xP, yP = c, -0.5
xQ, yQ = -c, -0.5

# Midpoint (vertex) V of latus rectum
xV = (xP + xQ) / 2
yV = (yP + yQ) / 2

# Length of latus rectum PQ
lengthPQ = np.sqrt((xP - xQ)**2 + (yP - yQ)**2)

# Parabola parameter a_p = lengthPQ / 4
a_p = lengthPQ / 4

# Parabola coefficient 2 * sqrt(3)
coeff = 2 * np.sqrt(3)

# Constant in parabola equation x^2 - 2√3 y = constant
constant = -coeff * yV

print(f"Parabola equation: x^2 - 2√3 y = {constant:.4f}")

# Prepare plot

theta = np.linspace(0, 2*np.pi, 400)
x_ellipse = a_ellipse * np.cos(theta)
y_ellipse = b_ellipse * np.sin(theta)

# Parabola: x^2 = 2√3 (y + 0.5)
# => y = (x^2) / (2√3) - 0.5
x_parabola = np.linspace(-4, 4, 400)
y_parabola = (x_parabola**2) / (2 * np.sqrt(3)) - 0.5

plt.figure(figsize=(8, 6))
plt.plot(x_ellipse, y_ellipse, label='Ellipse: $x^2 + 4y^2 = 4$', color='blue')
plt.plot(x_parabola, y_parabola, label='Parabola', color='red')

# Mark latus rectum endpoints and vertex
plt.scatter([xP, xQ], [yP, yQ], color='green', label='Latus Rectum Endpoints P, Q')
plt.scatter(xV, yV, color='purple', label='Vertex V')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title('Ellipse and Parabola with Latus Rectum')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Save the plot
plt.savefig('fig14.png', dpi=300)
plt.show()
