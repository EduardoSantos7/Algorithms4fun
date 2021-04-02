"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    seen = None

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        temp = head
        stack = []

        while temp:
            if temp.child:
                if temp.next:
                    stack.append(temp.next)

                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None

            if not temp.next and stack:
                temp.next = stack.pop()
                temp.next.prev = temp

            temp = temp.next

        return head
