import numpy as np
import matplotlib.pyplot as plt

# Step 1: Solve (p+1)(p^2+1)^2 = 0 in Python
# Only real solution is p = -1
p = -1
print(f"Real solution: p = {p}")

# Step 2: Define lines
# L1: p*(p^2+1)*x - y + q = 0 => y = p*(p^2+1)*x + q
# L2: (p^2+1)^2*x + (p^2+1)*y + 2q = 0 => y = -((p^2+1)^2 * x + 2q)/(p^2+1)
q = 1  # arbitrary value
x = np.linspace(-5, 5, 400)

y1 = p*(p**2 + 1)*x + q
y2 = -((p**2 + 1)**2 * x + 2*q)/(p**2 + 1)

# Step 3: Common perpendicular
# Slope of parallel lines: m = -2
# Slope of perpendicular line: m_perp = 1/2
m_perp = 1 / 2
y_mid = (y1[200] + y2[200]) / 2  # midpoint at x=0
x_perp = np.linspace(-5, 5, 400)
y_perp = m_perp * x_perp + y_mid

# Step 4: Plot lines and perpendicular
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
