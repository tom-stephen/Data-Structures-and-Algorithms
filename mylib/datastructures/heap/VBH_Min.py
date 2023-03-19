class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def remove(self):
        if self.is_empty():
            return None
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._percolate_down(0)
        return min_item
    
    def delete(self, item):
        if self.is_empty():
            return None
        index = self.heap.index(item)
        self.heap[index] = self.heap[-1]
        del self.heap[-1]
        self._percolate_down(index)
    
    def extract_min(self):
        if self.is_empty():
            return None
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._percolate_down(0)
        return min_item

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    @staticmethod
    def heapsort(arr):
        n = len(arr)
        # Build min heap
        for i in range(n // 2 - 1, -1, -1):
            MinHeap._percolate_down(arr, i, n)
        # Heap sort
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            MinHeap._percolate_down(arr, 0, i)
        return arr

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
