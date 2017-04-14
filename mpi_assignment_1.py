from mpi4py import MPI

#Get Process Info
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank % 2 == 0: #Even Rank, print Hello
	print('Hello from process %d' % rank)
else: #Odd Rank, print Goodbye
	print('Goodbye from process %d' % rank)