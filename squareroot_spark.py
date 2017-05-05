from pyspark import SparkContext
from operator import add
import re

# Calculate the Average of all square roots within a range
# Map ech element in RDD to roots. 
# Then reduce to sum and divide by key count

if __name__ == '__main__': 
    sc = SparkContext("local", "sqrt avg")

    roots = sc.parallelize(range(1, 1001)).map(lambda x: x ** 0.5)
    avg = roots.fold(0, add) / roots.count()

    print("Avg of Square Roots below 1001:", avg)
