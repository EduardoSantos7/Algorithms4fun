# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        left, right = head, head.next

        new_head = right or head

        while right:
            # swap
            left.next = right.next
            right.next = left
            # keep right in as right
            right, left = left, right

            # move 2 nodes forward
            left = right.next
            right.next = left.next if (left and left.next) else right.next
            right = left.next if left else None

        return new_head
