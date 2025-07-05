# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, node: Optional[ListNode]) -> List[Optional[ListNode]]:
        p1, p2, counter = node, node.next, 1

        while p2 != node:
            p1 = p2
            p2 = p2.next
            counter += 1
        
        temp = p2
        for _ in range(1, ceil(counter / 2)):
            temp = temp.next
        
        new_list = temp.next
        temp.next = p2
        p1.next = new_list

        return [node, new_list]