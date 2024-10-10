import ctypes

# Load the shared object file
add_lib = ctypes.CDLL("./add.so")

# Define argument and return types for the add function
add_lib.add.argtypes = [ctypes.c_double, ctypes.c_double]
add_lib.add.restype = ctypes.c_double

# Call the function
result = add_lib.add(3.0, "hello")
print(result)
