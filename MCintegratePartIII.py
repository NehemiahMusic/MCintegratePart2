import numpy as np
import MCintegratePartII as mc

def f(x):
    return (x**2)

print(f(.5))
n = 1000
x0 = 0
x1 = 1 
y0 = 0 
y1 = 1
ans = mc.MCinteg(f, x0, x1, y0, y1, n)
print(ans) 