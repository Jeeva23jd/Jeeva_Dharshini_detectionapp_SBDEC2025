import numpy as np

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Element-wise Multiplication:\n", m1 * m2)
print("Matrix Multiplication:\n", np.dot(m1, m2))
print("Transpose:\n", m1.T)