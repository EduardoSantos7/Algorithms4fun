# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use a monothonic decreasin stack to filter the nodes
        stack = [head]
        current = head.next
        while current:
            while stack and current.val > stack[-1].val:
                stack.pop()
            stack.append(current)
            current = current.next
        # Traverse the stack to link the node in it
        for i in range(len(stack)):
            if i < len(stack) - 1:
                stack[i].next = stack[i+1]
            else:
                stack[i].next = None
        # return the head of the new list
        return stack[0]