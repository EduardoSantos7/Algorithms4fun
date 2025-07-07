# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Get the middle of the list
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        # Reverse 2nd half
        curr, prev = p1, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # Perform sum and get max
        start = head
        _max = 0
        while prev:
            _max = max(_max, start.val + prev.val)
            prev = prev.next
            start = start.next
    
        return _max