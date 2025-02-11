"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # We'll track the smallest (head) and the previously visited node (prev)
        self.head = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # If prev is set, link it with the current node
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                # If prev is None, it means 'node' is the smallest so far -> head
                self.head = node
            self.prev = node
            inorder(node.right)

        # Perform in-order traversal, linking nodes
        inorder(root)

        # Close the circular loop
        # self.head is the smallest node, and self.prev is the largest node
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head
