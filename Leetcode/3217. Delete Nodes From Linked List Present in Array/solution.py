# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        mem = set(nums)
        dummy_node = ListNode(next = head)
        new_head = dummy_node
        while dummy_node.next != None:
            if dummy_node.next.val in mem:
                dummy_node.next = dummy_node.next.next
            else:
                dummy_node = dummy_node.next

        return new_head.next