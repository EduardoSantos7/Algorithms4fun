# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # Find frequency of the values
        temp = head
        memory = dict()
        while temp:
            memory[temp.val] = memory.get(temp.val, 0) + 1
            temp = temp.next
        # For values with frequency bigger than 2, remove the node
        current = head
        prev = None
        while current:
            if memory[current.val] > 1:
                if prev:
                    prev.next = current.next
                else:
                    head = head.next
            else:
                prev = current

            current = current.next
        
        return head