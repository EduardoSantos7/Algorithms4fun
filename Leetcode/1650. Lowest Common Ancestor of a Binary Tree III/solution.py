"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen_parents = {}
        temp = p
        # Traverse the tree upward from p storing all the parent nodes seen
        while temp:
            # if any of these parent nodes is equals to q then return q
            if temp.val == q.val:
                return q
            seen_parents[temp.val] = temp
            temp = temp.parent
        # Now from q traverse upwards but looking for seen nodes
        temp = q
        while temp:
            # if current parent node seen return it
            if temp.val in seen_parents:
                return seen_parents[temp.val]
            temp = temp.parent