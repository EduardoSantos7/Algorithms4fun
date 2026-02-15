# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        ptr = head
        carry = 0

        while ptr:
            if ptr.next == None:
                ptr.val += 1
                if ptr.val > 9:
                    ptr.val = 0
                    carry = 1
            else:
                stack.append(ptr)

            ptr = ptr.next

        if not carry:
            return head

        i = len(stack) - 1
        while carry and i >= 0:
            stack[i].val += 1
            if stack[i].val > 9:
                stack[i].val = 0
            else:
                carry = 0

            i -= 1

        if carry:
            head = ListNode(1, head)

        return head
