import numpy as np

arr = np.array([5, 10, 15, 20, 25])
mask = arr > 12

print("Array:", arr)
print("Mask:", mask)
print("Filtered:", arr[mask])