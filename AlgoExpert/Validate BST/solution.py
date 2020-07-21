# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_=float('-inf'), max_=float('inf')):
    if not tree:
        return True

    if tree.value < min_ or tree.value >= max_:
        return False

    return validateBst(
        tree.left, min_=min_, max_=tree.value) and validateBst(
            tree.right, min_=tree.value, max_=max_)
