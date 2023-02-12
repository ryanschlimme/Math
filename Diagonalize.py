from sympy import *

M = Matrix([[1, 0, 8, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 8],
            [8, 0, 0, 1]])

print("Matrix:", M)
P, D = M.diagonalize()
print("Diagonal:", D)
