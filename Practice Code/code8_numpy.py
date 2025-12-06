import numpy as np

np.random.seed(0)
print("Random Integers:\n", np.random.randint(1, 10, (2, 3)))
print("Random Floats:\n", np.random.rand(2, 3))
print("Normal Distribution:\n", np.random.randn(5))