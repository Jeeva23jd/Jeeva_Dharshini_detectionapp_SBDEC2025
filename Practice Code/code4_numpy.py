import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Element at (0,1):", arr[0, 1])
print("2nd Row:", arr[1, :])
print("3rd Column:", arr[:, 2])
print("Slice (2x2):\n", arr[:2, :2])