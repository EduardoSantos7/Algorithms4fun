def nodeDepths(root):
    stack = [(root, 0)]
    depth = 0
    depths_sum = 0
    while stack:
        node, depth = stack.pop()
        if node:
            depths_sum += depth
            stack.extend([(node.left, depth + 1), (node.right, depth + 1)])
    return depths_sum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
