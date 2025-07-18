# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        p1, p2, odd, even = head, head.next, 0, 0

        while p1:
            if p1.val > p2.val:
                even += 1
            elif p1.val < p2.val:
                odd += 1

            p1 = p2.next
            p2 = p1.next if p1 else None

        return "Tie" if even == odd else ("Even" if even > odd else "Odd")