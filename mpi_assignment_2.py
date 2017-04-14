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
	buffer[0] = input("Please enter something: ")
	
	#Make sure there is more than 1 process
	if size > 1:
		comm.Send(buffer, dest=rank+1)
		comm.Recv(buffer, source=size-1)
	
	print("Final Result:", buffer[0])
else:

	comm.Recv(buffer, source=rank-1)
	
	print("Rank:", rank, "Received:", buffer[0], "Result:", buffer[0]*rank)
	
	buffer[0] *= rank
	
	#Decide to prop up to return to origin
	if rank != size - 1:
		comm.Send(buffer, dest=rank+1)
	else:
		comm.Send(buffer, dest=0)