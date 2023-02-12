import numpy as np
from scipy.integrate import nquad


def integrand(x, y, a, b):
    return a * x + (b * x / y ** 2)


a = np.sqrt(2)
b = 4

# nquad is used for numerically calculating integrals (n=1 for single, n=2 for double, and so on)
# nquad(defined_integrand, [[xbounds],[ybounds],...], args=(function arguments))
I = nquad(integrand, [[0, 1], [0, np.inf]], args=(a, b))
print(I)
