import numpy as np
dx = 0.0001 # for precision. The smaller, the more precise, more computationally heavy
def grad(f, x: float):
    return (f(x + dx) - f(x))/(dx)

def integrate(f, lower: float, upper: float):
#    assert lower <= upper, "Please Input Valid Boundaries"
    sum = 0
    if lower < upper:
        for i in np.arange(lower, upper, dx):
            sum += f(i) * dx
        return sum
    else:
        for i in np.arange(upper, lower, dx):
            sum += f(i) * dx
        return -sum