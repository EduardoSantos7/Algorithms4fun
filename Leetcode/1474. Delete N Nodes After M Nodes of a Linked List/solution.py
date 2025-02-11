# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        keep_mover = ListNode(next=head)
        delete_mover = head
        keep_count = 0

        while keep_mover and delete_mover:
            for _ in range(m):
                if not keep_mover:
                    break
                
                keep_mover = keep_mover.next
            
            delete_mover = keep_mover

            for _ in range(n):
                if not delete_mover:
                    break
                
                delete_mover = delete_mover.next
            
            if keep_mover:
                keep_mover.next = delete_mover.next if delete_mover else None
            

        return head