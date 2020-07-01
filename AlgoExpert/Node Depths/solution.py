def bfs(root):
    # None represents the end of the level
    queue = [root, None]
    depths = 0
    level = 0
    was_none = False
    while queue:
        node = queue.pop(0)
        if not node:
            if was_none:
                break
            queue.append(None)
            was_none = True
            level += 1
            continue
        was_none = False
        depths += level
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return depths


def nodeDepths(root):
    if not root:
        return 0

    return bfs(root)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
