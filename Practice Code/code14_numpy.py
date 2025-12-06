import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

# Save array
np.save("my_array.npy", arr)

# Load array
loaded = np.load("my_array.npy")

print("Original Array:\n", arr)
print("Loaded Array:\n", loaded)