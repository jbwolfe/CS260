from abstractHeap import Heap
import math

"""Heap structure based off of the abstract class Heap."""
class MinHeap(Heap):
	def __init__(self, store):
		self.store = store # Store is usually an array
		self.heapSize = len(self.store)

	def __str__(self):
		""" Return self.store and the size. """
		return 'HEAP: ' + str(self.store) + '\n\tSIZE: ' + str(self.heapSize) + '\n'

	def __len__(self):
		""" Return the length of the store. """
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
		if left < self.heapSize and self.store[left] < self.store[i]:
			largest = left
		else:
			largest = i
		if right < self.heapSize and self.store[right] < self.store[largest]:
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
		"""WORK ON ME!!!"""
		pass

	def heapMinimum(self):
		pass
		return self.store[0]

	def extractMin(self):
		if self.heapSize < 1:
			try:
				pass
			except TypeError:
				raise TypeError('Heap underflow')
		minimum = self.store[0]
		self.store[0] = self.store[self.heapSize-1]
		self.heapSize = self.heapSize - 1
		self.heapify(0)
		return minimum

	def extractMax(self):
		pass
		pass

	def increaseKey(self, i, key):
		if key < self.store[i]:
			try:
				pass
			except TypeError:
				raise TypeError('new key is smaller than current key')
		self.store[i] = key
		while i > 0 and self.store[self.getParent(i)] > self.store[i]:
			self.exchange(i, self.getParent(i))
			i = self.getParent(i)

	def heapInsert(self, key):
		self.heapSize = self.heapSize + 1
		self.store.append(1)
		self.increaseKey(self.heapSize-1, key)

	def bubbleUp(self):
		pass
		pass

	def peek(self):
		pass
		return self.store[0]

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
				treeStruc += '\n\t\t' + str(self.store[i]) + ' -> ' + str(self.store[self.getLeftChild(i)]) +  ' [color = "blue"];'
			else:
				# treeStruc += '\n\t\t' + 'None' + str(i) + ' [label = " "];' # View children as empty nodes
				treeStruc += '\n\t\t' + 'None' + str(i) + ' [shape = point];' # View children as points
				treeStruc += '\n\t\t' + str(self.store[i]) + ' -> ' + 'None' + str(i) +  ' [color = "blue"];'

			if self.getRightChild(i) < len(self.store):
				treeStruc += '\n\t\t' + str(self.store[i]) + ' -> ' + str(self.store[self.getRightChild(i)]) +  ' [color = "red"];'
			else:
				# treeStruc += '\n\t\t' + 'None' + str(i+len(self.store)) + ' [label = " "];' # View children as empty nodes
				treeStruc += '\n\t\t' + 'None' + str(i+len(self.store)) + ' [shape = point];' # View children as points
				treeStruc += '\n\t\t' + str(self.store[i]) + ' -> ' + 'None' + str(i+len(self.store)) +  ' [color = "red"];'
		treeStruc += '\n\n\t\tlabel="Josh\'s Heap Priority Queue";\n\t}\n}'
		f.write(treeStruc)
		f.close()
		os.system('dot -Tpng -O vizData')
		os.system('eog vizData.png')
