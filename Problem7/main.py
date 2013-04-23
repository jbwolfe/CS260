from priorityHeap import PriorityHeap
import sys
import os

"""START MODULE"""
def main(argv):
	PQ = create(argv)
	displayMenu(PQ)
	queuesMod(PQ)

"""Create random data, priorities, and the priority queue itself"""
def create(argv):
	argc = len(argv)
	if argc != 3:
		print("USAGE: python3 {0} <bufferSize> <numberOfPriorities> \n".format(argv[0]))
		sys.exit()

	bufferSize = argv[1]
	numberOfPriorities = argv[2]
	numberOfSwaps = str(((int(bufferSize)//2)))

	# print('\nbufferSize: ', bufferSize)
	# print('numberOfPriorities: ', numberOfPriorities)
	# print('numberOfSwaps', numberOfSwaps, '\n')

	# print('Generating data...\n')
	os.system('python3 makeIntegers.py ' + str(int(bufferSize)+1) + ' 1 1 ' + numberOfSwaps + ' > data.dat')
	os.system('python3 makeIntegers.py ' + str(int(numberOfPriorities)+1) + ' 1 1 0 > priorities.dat')

	priorities = open('priorities.dat','r')
	data = open('data.dat','r')

	Plevel = list()
	Pdata = list()
	for PLine in priorities:
		Plevel.append(int(PLine.rstrip(' \n\t')))
	for DLine in data:
		Pdata.append(int(DLine.rstrip(' \n\t')))

	# print('\t   Data:\t', Pdata)
	# print('\tPriorities:\t', Plevel)

	data = list()
	# print('\n\tITEM\tPRIORITY')
	for i in range(0, len(Pdata), 1):
		# print('\t', Pdata[i], '\t  ', Plevel[i%(len(Plevel))])
		data.append((Plevel[i%(len(Plevel))],Pdata[i]))

	# print('\nBuilding Heap...\n')
	PQ = PriorityHeap(data, int(bufferSize), int(numberOfPriorities))
	# print(PQ)
	PQ.buildHeap()
	# print(PQ)

	return PQ

"""DISPLAY MODULE"""
def displayMenu(PQ):
	os.system('clear')  
	print('\n\t\t\tWELCOME TO PROBLEM 7 MINI-INTERPRETER\n\t\t\t\tPRIORITY QUEUE (HEAP)')
	print('\nPRIORITY QUEUE MODULE\n')
	print(' N XXX YYY \t---\t Create new queue with fixed buffer size XXX with YYY priorities')
	print(' E XXX YYY \t---\t Enqueue XXX with YYY priority')
	print(' D \t\t---\t Dequeue lowest priority')
	print(' V \t\t---\t View the queue (NOTE: (PRIORITY, DATA))')
	print(' E \t\t---\t EXIT\n')
	print(PQ)




"""PRIORITY QUEUE DRIVER MODULE"""
def queuesMod(PQ):

	exitOpt = True
	pqueue = PQ
	pqueue.heapMinimum()

	while exitOpt:
		flag = input('\n\nINPUT: ')

		""" CLEAR SCREEN & DISPLAY MENU"""
		if len(flag) == 0:
			displayMenu(pqueue)
			continue

		if flag[0].lower() == 'n':
			opt = flag.split()
			pqueue = create(opt)

		if flag[0].lower() == 'e':
			opt = flag.split()
			if len(opt) == 3: # WITH PRIORITIES
				pqueue.heapInsert((int(opt[2]),int(opt[1]))) # WITH PRIORITIES
			# if len(opt) == 2:
			# 	pqueue.heapInsert(int(opt[1]))
			else:
				confirm = input('Are you sure?  ')
				if confirm[0].lower() == 'y':
					os.system('clear')
					exitOpt = False
				else:
					continue

		if flag[0].lower() == 'd':
			print('Dequeueing: ',str(pqueue.extractMax()))

		if flag[0].lower() == 'v':
			# print('\n\tInternal View: ', pqueue)
			pqueue.externalView()


if __name__=='__main__':
	import sys
	sys.exit(main(sys.argv))
