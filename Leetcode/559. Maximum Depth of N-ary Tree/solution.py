"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node', count: int = 1) -> int:
        if not root:
            return 0

        depths = [self.maxDepth(child, count + 1) for child in root.children]
        depths.append(count)

        return max(depths)
