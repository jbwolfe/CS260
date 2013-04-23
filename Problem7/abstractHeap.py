from abc import ABCMeta, abstractmethod

class Heap(metaclass=ABCMeta):
	"""The heap class is based of off an array with
	 the following methods.

	Documentation and time complexity is included each method."""

	@abstractmethod
	def length(self):
		"""The LENGTH procedure returns the length of the store
		 in O(1) time."""

	@abstractmethod
	def getParent(self):
		"""For heaps based upon arrays, node values are stored in
		 an array and the indices of that array are considered the
		 node pointers. For example, the root node has index 0, the
		 left child of the root has index 1, the right child of the
		 root has index 2. In general, the index of the left child
		 of any node is one more than twice the index of its parent 
		 and the index of the right child of any node is one more 
		 than the index of the left child.

		To compute the parent index of a node n, simply subtract
		 one from n's index and then divide the result by two 
		 (integer division).

		The get- operations can obviously be performed in constant
		 time."""

	@abstractmethod
	def getLeftChild(self):
		"""For heaps based upon arrays, node values are stored in
		 an array and the indices of that array are considered the
		 node pointers. For example, the root node has index 0, the
		 left child of the root has index 1, the right child of the
		 root has index 2. In general, the index of the left child
		 of any node is one more than twice the index of its parent 
		 and the index of the right child of any node is one more 
		 than the index of the left child.

		To compute the parent index of a node n, simply subtract
		 one from n's index and then divide the result by two 
		 (integer division).

		The get- operations can obviously be performed in constant
		 time."""

	@abstractmethod
	def getRightChild(self):
		"""For heaps based upon arrays, node values are stored in
		 an array and the indices of that array are considered the
		 node pointers. For example, the root node has index 0, the
		 left child of the root has index 1, the right child of the
		 root has index 2. In general, the index of the left child
		 of any node is one more than twice the index of its parent 
		 and the index of the right child of any node is one more 
		 than the index of the left child.

		To compute the parent index of a node n, simply subtract
		 one from n's index and then divide the result by two 
		 (integer division).

		The get- operations can obviously be performed in constant
		 time."""

	@abstractmethod
	def heapify(self, i):
		"""This operation begins by ensuring the value at the root
		 of the heap is less than its children. If it is not, the 
		 root value is swapped with the minimum value, with respect 
		 to the children. The process continues by examining the 
		 child that received the root's value to ensure it is 
		 smaller than either of its children. If it is not, its 
		 value is swapped with the minimum value of its children 
		 and so on.

		The heapify operation takes Θ (log n) time, since the heap 
		 is a complete binary tree (and thus is balanced)."""

	@abstractmethod
	def buildHeap(self):
		"""The build-heap operation turns an unordered complete
		 binary tree in the heap. It begins by running heapify on
		 each parent of the leaves. It continues by running heapify
		 on each grandparent of the leaves, and so on. By working
		 from the leaves upward to the root, the smaller values
		 are guaranteed to bubble upwards, with the smallest value
		 ending up at the root.

		The build-heap operation takes 0 (n log n) time. Note that
		 this is an upper bound, not a tight bound."""

	@abstractmethod
	def heapsort(self):
		"""The HEAPSORT procedure takes time O(n log n), since the call to 
		 BUILDHEAP takes time O(n) and each of the n - 1 calls to HEAPIFY
		 takes O(log n)."""

	@abstractmethod
	def heapMaximum(self):
		"""The procedure HEAPMAXIMUM implements the maximum aperation
		 in O(1) time."""

	@abstractmethod
	def extractMax(self):
		"""To extract the minimum value of a heap (which is found 
		 at the root, one first saves a pointer to the root 
		 value. Next, the rightmost leaf in the lowest layer 
		 is pruned from the heap and its value is used to
		 replace the root's value. Finally, the heapify
		 operation is performed on the root to ensure heap
		 ordering is preserved.

		This is why an array is so convenient for storing values in
		 a heap. The index of the rightmost leaf in the lowest
		 layer is the last index of the array. If there are s elements in
		 the heap, the last index is s - 1.

		Pruning the rightmost leaf in the lowest layer devolves to
		 reducing the perceived size of the array. Note that the
		 array does not actually have to be reduced in size.

		Since pruning takes constant time, the entire extract-min
		 operation takes Θ (log n) time since the operation is
		 dominated by heapify."""

	@abstractmethod
	def heapMinimum(self):
		"""~~~
		 DOCUMENT THIS!
		 ~~~"""

	@abstractmethod
	def extractMin(self):
		"""To extract the minimum value of a heap (which is found 
		 at the root, one first saves a pointer to the root 
		 value. Next, the rightmost leaf in the lowest layer 
		 is pruned from the heap and its value is used to
		 replace the root's value. Finally, the heapify
		 operation is performed on the root to ensure heap
		 ordering is preserved.

		This is why an array is so convenient for storing values in
		 a heap. The index of the rightmost leaf in the lowest
		 layer is the last index of the array. If there are s elements in
		 the heap, the last index is s - 1.

		Pruning the rightmost leaf in the lowest layer devolves to
		 reducing the perceived size of the array. Note that the
		 array does not actually have to be reduced in size.

		Since pruning takes constant time, the entire extract-min
		 operation takes Θ (log n) time since the operation is
		 dominated by heapify."""

	@abstractmethod
	def increaseKey(self):
		"""The running time of INCREASEKEY on an n-element heap
		 is O(log n), since the path traced from the node update
		 in line 3 to the toor has length O (log n)."""

		"""To insert a value into a heap of size s, one bases one
		 places the new value into the heap at index s. The size
		 is then incremented to reflect the additional element.
		 The bubble-up operation is called on the new value to 
		 ensure it rises to the proper level in the heap.

		Insertion requires the heap be based upon a fillable 
		 array (for a bounded heap) or a dynamic array (for an 
		 unbounded heap)."""

	@abstractmethod
	def heapInsert(self):
		"""The running time of HEAPINSERT on on n-element heap
		 is O(log n)."""

	@abstractmethod
	def peek(self):
		"""The peek operation returns the value at the root 
		 of the heap."""

	@abstractmethod
	def isEmpty(self):
		"""This operation returns true if there are no 
		 elements in the heap and false otherwise."""

	@abstractmethod
	def exchange(self):
		"""The EXCHANGE procedure swaps two elements in
		 the store array.

		The EXCHANGE procedure performs in O(n) time."""

	@abstractmethod
	def internalView(self):
		"""View the heap as the underlying data structure in terminal.
		 (Usually an array)"""

	@abstractmethod
	def externalView(self):
		"""View the heap as the external, abstract tree using graphviz.
		 """
