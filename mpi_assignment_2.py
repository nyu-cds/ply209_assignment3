from mpi4py import MPI
import numpy as np

#Daisy chain-multiply a user value for each process running and print the result

#Get Process Info
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#Set Buffer value size of 1
buffer = np.zeros(1)

#Rank 0 Starting process
if rank == 0:
	inp = None
	
	#Continuously ask for correct input: Integer less than 100
	while inp is None or buffer[0] >= 100:
		inp = input("Please insert an integer less than 100: ")
		try:
			buffer[0] = int(inp)
		except ValueError:
			inp = None
	
	#Make sure there is more than 1 process
	if size > 1:
		comm.Send(buffer, dest=rank+1)
		comm.Recv(buffer, source=size-1)
	
	print("Final Result:", buffer[0])
else:
	#Receive from previous rank
	comm.Recv(buffer, source=rank-1)
	
	print("Rank:", rank, "Received:", buffer[0], "Result:", buffer[0]*rank)
	
	buffer[0] *= rank
	
	#Decide to prop up to return to origin
	comm.Send(buffer, dest=(rank + 1) % size)