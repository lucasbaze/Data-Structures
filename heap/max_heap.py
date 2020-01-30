class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # Add the item to the end of the array
        self.storage.append(value)
        # Bubble it up if necessary, passing in the last index (which is the item just added)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        # Swap the last and first item
        self._swap(0, self.get_size() - 1)

        # Delete the last item (which is now the first item)
        item = self.storage.pop()

        # Shift the first item down to where it should go
        self._sift_down(0)

        return item

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # while the parent is smaller than the item just added, swap them
        while self._hasParent(index) and self._getParent(index) < self.storage[index]:
            self._swap(self._getParentIndex(index), index)
            index = self._getParentIndex(index)

    def _sift_down(self, index):
        # While the index is less than the left or right branch
        # Move them downward
        while self._hasLeftChild(index):
            largerChildIndex = self._getLeftChildIndex(index)
            if self._hasRightChild(index) and self._getRightChild(index) > self._getLeftChild(index):
                largerChildIndex = self._getRightChildIndex(index)
            
            if self.storage[index] > self.storage[largerChildIndex]:
                break
            else:
                self._swap(largerChildIndex, index)
                
            index = largerChildIndex
                

    # Helper methods

    def _getParentIndex(self, index):
        return (index - 1) // 2
    def _getLeftChildIndex(self, index):
        return index * 2 + 1
    def _getRightChildIndex(self, index):
        return index * 2 + 2


    def _hasParent(self, index):
        return self._getParentIndex(index) >= 0
    def _hasLeftChild(self, index):
        return self._getLeftChildIndex(index) < self.get_size()
    def _hasRightChild(self, index):
        return self._getRightChildIndex(index) < self.get_size()


    def _getParent(self, index):
        return self.storage[self._getParentIndex(index)]
    def _getLeftChild(self, index):
        return self.storage[self._getLeftChildIndex(index)]
    def _getRightChild(self, index):
        return self.storage[self._getRightChildIndex(index)]

    def _swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp