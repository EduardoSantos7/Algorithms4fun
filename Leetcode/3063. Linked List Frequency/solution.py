# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mem = dict()

        while head != None:
            mem[head.val] = mem.get(head.val, 0) + 1
            head = head.next

        new_head = ListNode()
        temp = new_head
        for _, count in mem.items():
            new_node = ListNode(count)
            temp.next = new_node
            temp = temp.next

        return new_head.next