from maxHeap import MaxHeap
from minHeap import MinHeap


# a = [6, 5, 7, 4, 8, 3, 9, 2, 10, 1]
# a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# a = [1,2,3,4,5,6,7,8,9,10]
# a = [5,4,3,2,1]
# a = [1,2,3,4,5]
# a = [4,3,2,1]
# a = [1,2,3,4]

heap = MaxHeap(a)
# heap = MinHeap(a)
print(heap)
heap.buildHeap()
print(heap)
# heap.heapsort()
# print(heap)
heap.heapInsert(17)
heap.heapInsert(6)
heap.heapInsert(12)
heap.heapInsert(13)
heap.heapInsert(0)
# heap.heapInsert(5)
print(heap)
print(heap.heapMaximum())
print(heap)
print(heap.extractMax())
print(heap)
print(heap.increaseKey(6,17))
print(heap)
heap.externalView()