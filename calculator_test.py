# -----------------------------------------------------------------------------
# calculator_test.py
# ----------------------------------------------------------------------------- 
'''
	Original runtime: 1.62685723383s
	Improved runtime: 0.0130872047063s
	Relative speedup: 124.308992664
'''

import numpy as np
import calculator as calc
import timeit

M = 10**3
N = 10**3

A = np.random.random((M,N))
B = np.random.random((M,N))

C = calc.hypotenuse(A,B)
D = calc.hypotenuse2(A,B)

assert (C==D).all(), "Hypotenuse2 not correct"

print(timeit.timeit("calc.hypotenuse(A,B)", setup="from __main__ import A,B,calc", number=1))
print(timeit.timeit("calc.hypotenuse2(A,B)", setup="from __main__ import A,B,calc", number=1))