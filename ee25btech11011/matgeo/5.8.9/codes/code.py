import ctypes

# Load DLL (adjust filename/path as needed)
lib = ctypes.CDLL('./cod10.dll')

# Declare function argument and return types
lib.solve.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.solve.restype = None

# Prepare ctypes int variables to hold results
l = ctypes.c_int()
b = ctypes.c_int()

# Call the solve function from the DLL
lib.solve(ctypes.byref(l), ctypes.byref(b))

length = l.value
breadth = b.value

if length == -1 or breadth == -1:
    print("No valid solution found.")
else:
    print(f"Length = {length}, Breadth = {breadth}")
