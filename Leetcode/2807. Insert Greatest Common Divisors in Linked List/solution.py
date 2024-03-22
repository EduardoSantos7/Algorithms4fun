# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = head
        front = head.next

        while front:
            greatest_common_divisor = self._get_greatest_common_divisor(back.val, front.val)
            new_node = ListNode(greatest_common_divisor, front)
            back.next = new_node

            back = front
            front = front.next
        
        return head
    
    def _get_greatest_common_divisor(self, a, b):
        while b:
            a, b = b, a%b
        return a