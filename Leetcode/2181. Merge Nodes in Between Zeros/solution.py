# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use two pointers to find the two zeros, count the node values in between
        # when the second zero is found make the value of the first zero the accumulated value
        # and its next pointer to the second zero, the last zero is set to None
        first_zero = head
        second_zero = head
        accum = 0

        while second_zero:
            if second_zero.val == 0 and second_zero != first_zero:
                second_zero = second_zero.next if second_zero.next else None
                first_zero.val = accum
                first_zero.next = second_zero
                first_zero = first_zero.next
                accum = 0
            else:
                accum += second_zero.val
                second_zero = second_zero.next

        return head
