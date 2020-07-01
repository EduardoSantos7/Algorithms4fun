def nodeDepths(root):
    return dfs(root, 0)


def dfs(root, depth):
    if not root:
        return 0
    return depth + dfs(root.left, depth + 1) + dfs(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
