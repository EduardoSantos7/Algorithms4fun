# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        answer = []
        stack = []

        index = 0
        while head:
            current = head.val
            answer.append(0)

            while stack and stack[-1][0] < current:
                last_val = stack.pop()
                answer[last_val[1]] = current

            stack.append((current, index))
            index += 1
            head = head.next

        return answer
