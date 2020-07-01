# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(root, current_sum, sums):
    new_sum = root.value + current_sum
    # Leaf node
    if not root.left and not root.right:
        sums.append(new_sum)
    else:
        if root.left:
            dfs(root.left, new_sum, sums)
        if root.right:
            dfs(root.right, new_sum, sums)


def branchSums(root):
    if not root:
        return []
    sums = []
    dfs(root, 0, sums)
    return sums
