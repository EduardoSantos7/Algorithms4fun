def invertBinaryTree(tree):
    queue = [tree]

    while queue:
        node = queue.pop(0)

        temp = node.right
        node.right = node.left
        node.left = temp

        if node.right:
            queue.append(node.right)

        if node.left:
            queue.append(node.left)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
