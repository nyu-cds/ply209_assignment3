from itertools import repeat, chain, permutations

#Generate :n-length binary string sequences with k zero-bits
#ex: (4,3) -> {'0100', '0001', '0010', '1000'}
def zbits(n, k):
	# Assert k < n.
	assert k <= n, "Please make Num of 0s smaller than sequence length"

	#Make a string list iterator of correct 1's and zeros
	init = chain(repeat('0',k), repeat('1', n - k))

	#Get Permutations of string
	ans = {"".join(item) for item in permutations(init,n)}

	return ans

#Tests
if __name__ == '__main__':
	assert zbits(4, 3) == {'0100', '0001', '0010', '1000'}, "Test 1 (4,3) failed"
	assert zbits(4, 1) == {'0111', '1011', '1101', '1110'}, "Test 2 (4,1) failed"
	assert zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}, "Test 3 (5,4) failed"