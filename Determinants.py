import numpy as np
from scipy import linalg

M = np.array([[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])

print("Matrix: \n", M)
print("Determinant \n", linalg.det(M))
