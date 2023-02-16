from sympy import *
import numpy as np

M = Matrix([[0, np.sqrt(2), 0],
            [-1*np.sqrt(2), 0, np.sqrt(2)],
            [0, -1*np.sqrt(2), 0]])

print("Matrix:", M)
P, D = M.diagonalize()
print("Diagonal:", D)
