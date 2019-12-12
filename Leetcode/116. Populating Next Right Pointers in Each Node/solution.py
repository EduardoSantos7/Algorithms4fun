"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = [(root, None)]

        while q:
            current, parent = q.pop(0)

            # Each parent node links his children
            if current.left:
                current.left.next = current.right

            # If the current node has a parent and his parent already linked him
            # Then just add it children
            if parent and current.next:
                # This nodes always has either both nodes or none
                if current.left:
                    q.append((current.left, current))
                    q.append((current.right, current))

            elif not current.next:
                # If your parent hasn't a nextt value that means you're in the border
                # so you don't have a next value neither.
                current.next = parent.next.left if parent and parent.next else None
                if current.left:
                    q.append((current.left, current))
                    q.append((current.right, current))
        return root
