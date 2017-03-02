# -----------------------------------------------------------------------------
# calculator.py
# ----------------------------------------------------------------------------- 
'''
	Original runtime: 1.62685723383s
	Improved runtime: 0.0130872047063s
	Relative speedup: 124.308992664
	
	Improvements: Honestly, the nested for loops clearly killed the performance of the functions. 
	Using inbuilt numpy functions should resolve this.
	multiply(x,x) = np.square(x)
	add(xx,yy) = np.add(xx,yy)
	sqrt(zz) = np.sqrt(zz)
	
	Improvements made to hypotenuse2() which was compared to hypotenuse()
	
	Output of line_profiler on all functions: 
	*To run, uncomment @profile decorators and run: kernprof -l -v calculator_test.py
	
	Wrote profile results to calculator_test.py.lprof
	Timer unit: 3.95062e-07 s

	Total time: 1.18218 s
	File: calculator.py
	Function: add at line 117

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
	   117                                           @profile
	   118                                           def add(x,y):
	   119                                               """
	   120                                               Add two arrays using a Python loop.
	   121                                               x and y must be two-dimensional arrays of the same shape.
	   122                                               """
	   123         1            6      6.0      0.0      m,n = x.shape
	   124         1           56     56.0      0.0      z = np.zeros((m,n))
	   125      1001          992      1.0      0.0      for i in range(m):
	   126   1001000       836546      0.8     28.0          for j in range(n):
	   127   1000000      2154791      2.2     72.0              z[i,j] = x[i,j] + y[i,j]
	   128         1            2      2.0      0.0      return z

	Total time: 2.40864 s
	File: calculator.py
	Function: multiply at line 130

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
	   130                                           @profile
	   131                                           def multiply(x,y):
	   132                                               """
	   133                                               Multiply two arrays using a Python loop.
	   134                                               x and y must be two-dimensional arrays of the same shape.
	   135                                               """
	   136         2           11      5.5      0.0      m,n = x.shape
	   137         2          118     59.0      0.0      z = np.zeros((m,n))
	   138      2002         1881      0.9      0.0      for i in range(m):
	   139   2002000      1667159      0.8     27.3          for j in range(n):
	   140   2000000      4427697      2.2     72.6              z[i,j] = x[i,j] * y[i,j]
	   141         2            3      1.5      0.0      return z

	Total time: 1.10013 s
	File: calculator.py
	Function: sqrt at line 143

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
	   143                                           @profile
	   144                                           def sqrt(x):
	   145                                               """
	   146                                               Take the square root of the elements of an arrays using a Python loop.
	   147                                               """
	   148         1           24     24.0      0.0      from math import sqrt
	   149         1            6      6.0      0.0      m,n = x.shape
	   150         1           52     52.0      0.0      z = np.zeros((m,n))
	   151      1001          952      1.0      0.0      for i in range(m):
	   152   1001000       911264      0.9     32.7          for j in range(n):
	   153   1000000      1872417      1.9     67.2              z[i,j] = sqrt(x[i,j])
	   154         1            2      2.0      0.0      return z

	Total time: 7.16072 s
	File: calculator.py
	Function: hypotenuse at line 156

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
	   156                                           @profile
	   157                                           def hypotenuse(x,y):
	   158                                               """
	   159                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
	   160                                               x and y must be two-dimensional arrays of the same shape.
	   161                                               """
	   162         1      4599852 4599852.0     25.4      xx = multiply(x,x)
	   163         1      4483887 4483887.0     24.7      yy = multiply(y,y)
	   164         1      4472907 4472907.0     24.7      zz = add(xx, yy)
	   165         1      4568946 4568946.0     25.2      return sqrt(zz)

	Total time: 0.0111384 s
	File: calculator.py
	Function: hypotenuse2 at line 167

	Line #      Hits         Time  Per Hit   % Time  Line Contents
	==============================================================
	   167                                           @profile
	   168                                           def hypotenuse2(x,y):
	   169                                                  """
	   170                                                  Return sqrt(x**2 + y**2) for two arrays, a and b.
	   171                                                  x and y must be two-dimensional arrays of the same shape.
	   172                                                  """
	   173         1            9      9.0      0.0         assert x.shape == y.shape, "Please make x and y the same shape"
	   174
	   175         1         6467   6467.0     22.9         xx = np.square(x)
	   176         1         6734   6734.0     23.9         yy = np.square(y)
	   177         1         7837   7837.0     27.8         zz = np.add(xx, yy)
	   178         1         7147   7147.0     25.3         return np.sqrt(zz)
'''

import numpy as np

#@profile
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

#@profile
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

#@profile
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

#@profile
def hypotenuse2(x,y):
	"""
	Return sqrt(x**2 + y**2) for two arrays, a and b.
	x and y must be two-dimensional arrays of the same shape.
	"""
	assert x.shape == y.shape, "Please make x and y the same shape"
	
	xx = np.square(x)
	yy = np.square(y)
	zz = np.add(xx, yy)
	return np.sqrt(zz)