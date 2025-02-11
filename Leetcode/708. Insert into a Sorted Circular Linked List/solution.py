"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        if head == head.next:
            node = Node(insertVal, head)
            head.next = node
            return head

        # use two pointers to move
        _next = head.next
        moving_node = head

        while not (moving_node.val <= insertVal <= _next.val):
            moving_node, _next = _next, _next.next
            # reaching the end of the list
            if moving_node.val > _next.val:
                if insertVal > moving_node.val or insertVal <= _next.val:
                    node = Node(insertVal, _next)
                    moving_node.next = node
                    return head
            
            if moving_node == head:
                break

        node = Node(insertVal, _next)
        moving_node.next = node
        return head
        
        # 1, 2, 3 -> 0
        # 4, 5, 0 -> 6
        # 1, 2, 3, 4, 7 -> 6
        # 2, 3, 1 ->0
        # 3,4,5,6,7,8,9,1, 2 -> 2.5
        # 3,3,3 ->0