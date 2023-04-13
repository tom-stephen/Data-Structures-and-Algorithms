class MinHeap:
    
    def __init__(self, size = 0, array = None):
        self.heap = []
        if array is not None:
            self.heap = self._heapify(array)
        elif size > 0:
            self.heap = [] * size

    def getSize(self):
        return len(self.heap)
    
    def clear(self):
        self.heap.clear()

    def contains(self, item):
        return item in self.heap
    
    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    def delete(self, item):
        if self.isEmpty():
            return None
        index = self.heap.index(item)
        self.heap[index] = self.heap[-1]
        del self.heap[-1]
        self._percolate_down(index)

    def isEmpty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def _percolate_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._percolate_up(parent)

    def _percolate_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._percolate_down(smallest)

    def _parent(self, index):
        return (index - 1) // 2
    
    def _left_child(self, index):
        return index * 2 + 1
    
    def _right_child(self, index):
        return index * 2 + 2
    
    def _heapify(self, array):
        # transforms an array into a heap
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._percolate_down(i)
        return self.heap
    
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

    def sort(self):
        self.heap.sort()