# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # find the prev and next nodes in indexes from a and b in list1
        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        _next = prev
        for _ in range (b - a + 1):
            _next = _next.next

        # find the last element of list2
        _last = list2
        while _last.next is not None:
            _last = _last.next

        # switch pointers to point previous from a to head of list2 and next of b to next of last in list2
        prev.next = list2
        _last.next = _next.next

        return list1
