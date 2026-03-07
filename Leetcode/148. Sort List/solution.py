# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        first_half_list_head = head
        mid_node = self.find_mid_node(head)
        second_half_list_head = mid_node.next
        mid_node.next = None

        list_1 = self.sortList(first_half_list_head)
        list_2 = self.sortList(second_half_list_head)

        return self.merge(list_1, list_2)

    def merge(self, a, b):
        dummy = ListNode()
        dummy_head = dummy
        p1 = a
        p2 = b

        while p1 and p2:
            if p1.val <= p2.val:
                dummy.next = p1
                dummy = dummy.next
                p1 = p1.next
            else:
                dummy.next = p2
                dummy = dummy.next
                p2 = p2.next

        while p1:
            dummy.next = p1
            dummy = dummy.next
            p1 = p1.next
        
        while p2:
            dummy.next = p2
            dummy = dummy.next
            p2 = p2.next
        
        return dummy_head.next

    def find_mid_node(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow