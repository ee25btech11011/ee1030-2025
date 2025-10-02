# Solve the system:
# 3l - 5b = 6
# 2l + 3b = 61

def solve_system():
    # Try integer solutions since problem is simple and solution is integer
    for l in range(0, 100):
        for b in range(0, 100):
            if (3*l - 5*b == 6) and (2*l + 3*b == 61):
                return l, b
    return None, None

length, breadth = solve_system()

if length is None or breadth is None:
    print("No solution found.")
else:
    print(f"Length = {length}, Breadth = {breadth}")
