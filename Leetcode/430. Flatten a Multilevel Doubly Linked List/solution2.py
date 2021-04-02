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
        last = None

        while temp:

            if temp.child:
                last = temp.next
                temp.next = temp.child
                temp.child.prev = temp
                self.flatten(temp.next)
                temp.child = None

                if self.seen and last:
                    temp = self.seen
                    self.seen = None
                    temp.next = last
                    last.prev = temp
                    last = None

            if not temp.next:
                self.seen = temp

            temp = temp.next

        return head
