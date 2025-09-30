import ctypes
import numpy as np
import os

# Load the shared library
if os.name == "nt":
    lib = ctypes.CDLL("./code9.dll")
else:
    lib = ctypes.CDLL("./code9.so")

# Create a 2x2 NumPy array to hold the inverse
inv_matrix = np.zeros((2,2), dtype=np.double)

# Set the argument type for ctypes
lib.compute_inverse.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.compute_inverse.restype = None

# Call the C function with pointer to NumPy array
lib.compute_inverse(inv_matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

# Check if matrix is invertible
if np.all(inv_matrix == 0):
    print("Matrix is not invertible.")
else:
    print("Matrix is invertible.")
    print("Inverse matrix:\n", inv_matrix)
