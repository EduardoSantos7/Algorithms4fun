"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        temp = head
        while temp:
            new_node = Node(temp.val, None, None)
            # Insert the new node next to the original node
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next
        
        temp = head

        # Link the random pointer correctly
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        
        # Separate the two linked lists
        old_head = head
        new_head_ptr = head.next
        new_head = head.next

        while old_head:
            old_head.next = old_head.next.next
            new_head_ptr.next = new_head_ptr.next.next if new_head_ptr.next else None
            new_head_ptr = new_head_ptr.next
            old_head = old_head.next
        
        return new_head