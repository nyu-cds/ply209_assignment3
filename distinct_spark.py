from pyspark import SparkContext
import re

#Count the distinct number of words 
#Here I basically count all the keys during the map phase 
#but count the number of keys during the reduce phase

# remove any non-words and split lines into separate words
# finally, convert all words to lowercase
def splitter(line):
	line = re.sub(r'^\W+|\W+$', '', line)
	return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
	sc = SparkContext("local", "distinct_word_count")
	
	text = sc.textFile('pg2701.txt')
	words = text.flatMap(splitter)
	words_mapped = words.map(lambda x: (x,1))

	counts = words_mapped.reduceByKey(lambda x,y: 1) #Meaningless function, just aggregating keys
	print("Distinct Words:", counts.count())