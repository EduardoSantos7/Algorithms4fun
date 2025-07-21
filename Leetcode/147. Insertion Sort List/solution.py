# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head, current = ListNode(), head
        while current:
            prev = new_head
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            _next = current.next
            current.next = prev.next
            prev.next = current
            current = _next
        return new_head.next