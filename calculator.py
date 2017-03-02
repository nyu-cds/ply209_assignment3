# -----------------------------------------------------------------------------
# calculator.py
# ----------------------------------------------------------------------------- 
'''
	Original runtime: 1.62685723383s
	Improved runtime: 
    Relative speedup: 
	
	Improvements: Honestly, the nested for loops clearly killed the performance of the functions. 
	Using inbuilt numpy functions should resolve this.
	
	Output of line_profiler:
	
	Timer unit: 3.95062e-07 s
	
	Total time: 1.18659 s
	File: calculator.py
	Function: add at line 12

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
		12                                           @profile
		13                                           def add(x,y):
		14                                               """
		15                                               Add two arrays using a Python loop.
		16                                               x and y must be two-dimensional arrays of the same shape.
		17                                               """
		18         1            5      5.0      0.0      m,n = x.shape
		19         1           63     63.0      0.0      z = np.zeros((m,n))
		20      1001          950      0.9      0.0      for i in range(m):
		21   1001000       834386      0.8     27.8          for j in range(n):
		22   1000000      2168159      2.2     72.2              z[i,j] = x[i,j] + y[i,j]
		23         1            2      2.0      0.0      return z

	Total time: 2.41094 s
	File: calculator.py
	Function: multiply at line 25

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
		25                                           @profile
		26                                           def multiply(x,y):
		27                                               """
		28                                               Multiply two arrays using a Python loop.
		29                                               x and y must be two-dimensional arrays of the same shape.
		30                                               """
		31         2           10      5.0      0.0      m,n = x.shape
		32         2          111     55.5      0.0      z = np.zeros((m,n))
		33      2002         1850      0.9      0.0      for i in range(m):
		34   2002000      1684305      0.8     27.6          for j in range(n):
		35   2000000      4416415      2.2     72.4              z[i,j] = x[i,j] * y[i,j]
		36         2            4      2.0      0.0      return z

	Total time: 1.11406 s
	File: calculator.py
	Function: sqrt at line 38

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
		38                                           @profile
		39                                           def sqrt(x):
		40                                               """
		41                                               Take the square root of the elements of an arrays using a Python loop.
		42                                               """
		43         1           23     23.0      0.0      from math import sqrt
		44         1            5      5.0      0.0      m,n = x.shape
		45         1           58     58.0      0.0      z = np.zeros((m,n))
		46      1001          975      1.0      0.0      for i in range(m):
		47   1001000       923096      0.9     32.7          for j in range(n):
		48   1000000      1895809      1.9     67.2              z[i,j] = sqrt(x[i,j])
		49         1            1      1.0      0.0      return z

	Total time: 7.18763 s
	File: calculator.py
	Function: hypotenuse at line 51

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
		51                                           @profile
		52                                           def hypotenuse(x,y):
		53                                               """
		54                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
		55                                               x and y must be two-dimensional arrays of the same shape.
		56                                               """
		57         1      4579112 4579112.0     25.2      xx = multiply(x,x)
		58         1      4509777 4509777.0     24.8      yy = multiply(y,y)
		59         1      4496943 4496943.0     24.7      zz = add(xx, yy)
		60         1      4607861 4607861.0     25.3      return sqrt(zz)
'''

import numpy as np

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] + y[i,j]
    return z

def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] * y[i,j]
    return z

def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """
    from math import sqrt
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = sqrt(x[i,j])
    return z

#@profile
def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)