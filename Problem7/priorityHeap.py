from abstractHeap import Heap
import sys
import os
import math

"""Priority Queue as a Heap structure based off of the abstract class Heap."""
class PriorityHeap(Heap):
	def __init__(self, store, capacity, prioritySize):
		self.store = store # Store is usually an array
		self.heapSize = len(self.store)
		self.capacity = capacity
		self.priorityList = list()

		for i in range(1,prioritySize+1,1):
			self.priorityList.append(i)

	def __str__(self):
		return 'HEAP: ' + str(self.store) + '\n\tSIZE: ' + str(self.heapSize) + '/' + str(self.capacity)+ '\n\tNUMBER_OF_PRIORITIES: ' + str(len(self.priorityList)) + '\t' + str(self.priorityList) + '\n\tIS_FULL: ' + str(self.isFull()) + '\n'

	def __len__(self):
		return len(self.store)

	def length(self):
		pass
		return len(self.store)

	def getParent(self, i):
		if i == 0:
			return None
		if i%2 == 0:
			return math.floor(i/2)-1
		return math.floor(i/2)

	def getLeftChild(self, i):
		if i == 0:
			return 1
		return (2*i)+1

	def getRightChild(self, i):
		if i == 0:
			return 2
		return (2*i)+1+1

	def heapify(self, i):
		left = self.getLeftChild(i)
		right = self.getRightChild(i)
		if left < self.heapSize and self.store[left] > self.store[i]:
			largest = left
		else:
			largest = i
		if right < self.heapSize and self.store[right] > self.store[largest]:
			largest = right
		if largest != i:
			self.exchange(i, largest)
			self.heapify(largest)

	def buildHeap(self):
		self.heapSize = self.length()
		for i in range(math.floor(self.heapSize/2), 0,-1):
			self.heapify(i-1)

	def heapsort(self):
		for i in range (self.heapSize-1, 0, -1):
			self.exchange(0, i)
			self.heapSize -= 1
			self.heapify(0)		

	def heapMaximum(self):
		pass
		return self.store[0]

	def extractMax(self):
		if self.heapSize < 1:
			return None
		maximum = self.heapMaximum()
		self.store[0] = self.store[self.heapSize-1]
		self.heapSize = self.heapSize - 1
		self.heapify(0)
		self.store.pop()
		return maximum

	def heapMinimum(self):
		leftMostChild = 0
		while leftMostChild < len(self.store)-1:
			leftMostChild = (leftMostChild*2)+1
			if (leftMostChild*2)+1 > len(self.store)-1:
				break
		# find the minimum from [..., leftMostChild, ..., len(self.store)]
		for i in range(leftMostChild, len(self.store), 1):
			if self.store[i] < self.store[leftMostChild]:
				leftMostChild = i
		minimum = leftMostChild
		return minimum

	def extractMin(self):
		if self.heapSize < 1:
			return None
		minimum = self.heapMinimum()
		if minimum > 2:
			heapifyValue = self.getParent(self.getParent(minimum))
			self.heapSize = self.heapSize - 1
			del(self.store[minimum])
			self.heapify(heapifyValue)
			return minimum

	def increaseKey(self, i, key):
		if key < self.store[i]:
			try:
				pass
			except TypeError:
				raise TypeError('new key is smaller than current key')
		self.store[i] = key
		while i > 0 and self.store[self.getParent(i)] < self.store[i]:
			self.exchange(i, self.getParent(i))
			i = self.getParent(i)

	def fullHeapInsert(self, key):
		minimum = self.heapMinimum()
		self.store[minimum] = key
		self.increaseKey(minimum, key)

	def heapInsert(self, key):
		if key[0] in self.priorityList:
			if self.isFull():
				self.fullHeapInsert(key)
			else:
				self.heapSize = self.heapSize + 1
				self.store.append((1,1))
				self.increaseKey(self.heapSize-1, key)
		else:
			print('ERROR: Invalid priority, please use one of the following priorities...\n\t' + str(self.priorityList) + '\n')

	def peek(self):
		pass
		return self.store[0]

	def isFull(self):
		pass
		return self.heapSize == self.capacity

	def isEmpty(self):
		pass
		return self.heapSize() == 0

	def exchange(self, i, largest):
		temp = self.store[largest]
		self.store[largest] = self.store[i]
		self.store[i] = temp

	def internalView(self):
		print(self.store)
		return

	def externalView(self):
		f = open('vizData', 'w')

		treeStruc = 'digraph G {\n\tsubgraph cluster_0 {\n'

		for i in range(0, len(self.store), 1):

			if self.getLeftChild(i) < len(self.store):
				treeStruc += '\n\t\t' + '\"' + str(self.store[i]) + '\"' + ' -> ' + '\"' + str(self.store[self.getLeftChild(i)]) + '\"' +  ' [color = "blue"];'
			else:
				# treeStruc += '\n\t\t' + 'None' + str(i) + ' [label = " "];' # View children as empty nodes
				treeStruc += '\n\t\t' + 'None' + str(i) + ' [shape = point];' # View children as points
				treeStruc += '\n\t\t' + '\"' + str(self.store[i]) + '\"' + ' -> ' + 'None' + str(i) +  ' [color = "blue"];'

			if self.getRightChild(i) < len(self.store):
				treeStruc += '\n\t\t' + '\"' + str(self.store[i]) + '\"' + ' -> ' + '\"' + str(self.store[self.getRightChild(i)]) + '\"' +  ' [color = "red"];'
			else:
				# treeStruc += '\n\t\t' + 'None' + str(i+len(self.store)) + ' [label = " "];' # View children as empty nodes
				treeStruc += '\n\t\t' + 'None' + str(i+len(self.store)) + ' [shape = point];' # View children as points
				treeStruc += '\n\t\t' + '\"' + str(self.store[i]) + '\"' + ' -> ' + 'None' + str(i+len(self.store)) +  ' [color = "red"];'
		treeStruc += '\n\n\t\tlabel="Josh\'s Heap Priority Queue";\n\t}\n}'
		f.write(treeStruc)
		f.close()
		os.system('dot -Tpng -O vizData')
		os.system('eog vizData.png')