from mpi4py import MPI
import numpy as np

#Distributed sort
#Run program: mpiexec -n 4 python parallel_sorter.py
#Sorting less than memory limits doesn't save any time though

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
	# init random data
	input_size = 10000
	input_arr = np.random.randint(0, input_size, size = input_size)
	
	#Bucket Results into ranges corresponding to number of processes
	min = np.amin(input_arr)
	max = np.amax(input_arr)
	bins = np.linspace(min, max, num=size)
	digitized = np.digitize(input_arr, bins)
	
	#Thought I could optimize here since its O(mn) instead of O(n) but after some benchmarks, this one liner is the fastest since loops have too much overhead
	data = np.array([input_arr[digitized == i+1] for i in range(size)])
else:
	data = None

#Scatter to other processes
data = comm.scatter(data, root=0)

#Sort Part
#Note: Data for rank 0 is the first chunk
data = np.sort(data)

#Gather Results
data = comm.gather(data, root=0)

if rank == 0:
	#Concatenate results
	print(np.concatenate(data))