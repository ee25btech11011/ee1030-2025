import numpy as np

# Define the 2x2 matrix
A = np.array([[10, -2],
              [-5, 1]], dtype=float)

# Compute determinant
det = np.linalg.det(A)

# Check if matrix is invertible
if det == 0:
    print("Matrix is not invertible.")
else:
    print("Matrix is invertible.")

    # Compute inverse using the standard formula for 2x2
    inv_A = np.array([[A[1,1], -A[0,1]],
                      [-A[1,0], A[0,0]]]) / det

    # Display the inverse
    print("Inverse matrix:\n", inv_A)
