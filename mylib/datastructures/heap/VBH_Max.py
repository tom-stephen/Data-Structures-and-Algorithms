
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        max_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._percolate_down(0)
        return max_item

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    @staticmethod
    def heapsort(arr):
        n = len(arr)
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            MaxHeap._percolate_down(arr, i, n)
        # Heap sort
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            MaxHeap._percolate_down(arr, 0, i)
        return arr

    def _percolate_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._percolate_up(parent)

    def _percolate_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._percolate_down(largest)