# -----------------------------------------------------------------------------
# calculator_test.py
# ----------------------------------------------------------------------------- 
import numpy as np
import calculator as calc
import timeit

M = 10**3
N = 10**3

A = np.random.random((M,N))
B = np.random.random((M,N))

calc.hypotenuse(A,B)

print(timeit.timeit("calc.hypotenuse(A,B)", setup="from __main__ import A,B,calc", number=1))