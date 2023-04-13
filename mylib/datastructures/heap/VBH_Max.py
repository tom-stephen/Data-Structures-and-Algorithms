
class MaxHeap:
    
    def __init__(self, size = 0, array = None):
        self.heap = []
       
        if array is not None:
            self.heap = self._heapify(array)
        
        elif size > 0:
            self.heap = [] * size

    def getSize(self):
        return len(self.heap)
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def clear(self):
        self.heap.clear()

    def contains(self, value):
        return value in self.heap
    
    def insert(self, value):
        self.heap.append(value)
        self._percolate_up(len(self.heap) - 1)

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]
    
    def delete(self, value):
        if self.isEmpty():
            return None
        index = self.heap.index(value)
        self.heap[index] = self.heap[-1]
        del self.heap[-1]
        self._percolate_down(index)

    def sort(self):
        self.heap.sort()
        
    def print(self):
        # displays the content of the heap vector over 2 lines. 
        # First line is the index of the parent of each element. 
        # Second line are the elements themselves
        string = ""
        for i in range(len(self.heap)):
            string += str(self._parent(i)) + " "
        print(string)
        string = ""
        for i in range(len(self.heap)):
            string += str(self.heap[i]) + " "
        print(string)

    def _percolate_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._percolate_up(parent)
        
    def _percolate_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < self.getSize() and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.getSize() and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._percolate_down(largest)

    def _heapifyUp(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapifyUp(parent)

    def _heapifyDown(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < self.getSize() and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.getSize() and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapifyDown(largest)

    def _heapify(self, array):
        self.heap = array
        for i in range(len(array) - 1, -1, -1):
            self._heapifyDown(i)
        return self.heap
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _left(self, index):
        return 2 * index + 1
    
    def _right(self, index):
        return 2 * index + 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


    

    
    


