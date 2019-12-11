# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        out = None  # Head
        temp = None
        carry = 0

        while(p1 or p2 or carry):
            num_a = p1.val if p1 else 0
            num_b = p2.val if p2 else 0
            res = num_a + num_b + carry
            op = res % 10
            if out:
                n = ListNode(op)
                temp.next = n
                temp = temp.next
                carry = 1 if res >= 10 else 0
            else:
                out = ListNode(op)
                temp = out
                carry = 1 if res >= 10 else 0

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return out
