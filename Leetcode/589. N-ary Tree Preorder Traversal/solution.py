"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        if not root:
            return res

        temp = [root]

        while temp:
            node = temp.pop(0)
            res.append(node.val)
            temp = (node.children or []) + temp
        
        return res