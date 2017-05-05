from pyspark import SparkContext
from operator import mul
import re

#Calculate the factorial 1000
#RDD from 1 - 1001 and apply a "rolling multiply" on each element (starting with 1)

if __name__ == '__main__':
	sc = SparkContext("local", "1-1000 Folded Product")
	
	product = sc.parallelize(range(1, 1001)).fold(1, mul)

	print("1000 Factorial:", product)