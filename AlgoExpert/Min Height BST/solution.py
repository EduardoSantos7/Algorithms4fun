def minHeightBst(array):
    if array:
        mid = len(array) // 2
        root = BST(array[mid])
        root.left = minHeightBst(array[:mid])
        root.right = minHeightBst(array[mid + 1:])
        return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
