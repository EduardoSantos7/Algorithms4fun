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
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        temp = head
        last = None

        while temp:
            if temp.child:
                last = temp.next
                temp.next = temp.child
                temp.child.prev = temp
                self.flatten(temp.next)
                temp.child = None
            elif not temp.next and last:
                temp.next = last
                last.prev = temp
                last = None

            temp = temp.next

        return head
