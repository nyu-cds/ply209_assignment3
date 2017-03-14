import timeit
import pyximport
import setuptools
import numpy

pyximport.install(setup_args={"include_dirs":numpy.get_include()})

if __name__ == '__main__':
	#Timing It
	print(timeit.timeit("nbody(100, 'sun', 20000)", setup="from nbody_cython import nbody", number=1))
