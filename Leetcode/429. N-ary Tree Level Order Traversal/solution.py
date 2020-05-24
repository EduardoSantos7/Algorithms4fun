"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            current_level = []
            next_level = []

            for current_node in queue:
                current_level.append(current_node.val)
                next_level.extend(current_node.children)

            result.append(current_level)
            queue = next_level

        return result
