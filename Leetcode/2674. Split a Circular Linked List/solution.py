# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, node: Optional[ListNode]) -> List[Optional[ListNode]]:
        memory = []
        temp = node
        while not memory or temp != memory[0]:
            memory.append(temp)
            temp = temp.next

        half = ceil(len(memory) / 2)
        memory[-1].next = memory[half]
        memory[half-1].next = memory[0]
        return [memory[0], memory[half]]