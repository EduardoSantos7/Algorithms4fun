# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        x_parent, y_parent = None, None
        x_level, y_level, depth = 0, 0, 0
        while queue:
            depth += 1
            aux_queue = []
            for node in queue:
                same_parent = 0
                for child in [node.right, node.left]:
                    if child:
                        aux_queue.append(child)

                    if child and child.val == x:
                        x_parent = node.val
                        x_level = depth
                        same_parent += 1

                    if child and child.val == y:
                        y_parent = node.val
                        y_level = depth
                        same_parent += 1

                if same_parent == 2:
                    return False
                if x_level == y_level and x_parent != y_parent:
                    return True
                queue = aux_queue
