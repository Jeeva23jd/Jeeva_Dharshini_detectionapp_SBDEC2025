import numpy as np

arr = np.array([12, 5, 7, 2, 9])

print("Original:", arr)
print("Sorted:", np.sort(arr))
print("Indices that would sort:", np.argsort(arr))
print("Search position for 6:", np.searchsorted(arr, 6))