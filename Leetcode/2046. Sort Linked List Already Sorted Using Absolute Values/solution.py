# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        

        mem = dict()
        temp = head
        n = 0

        while temp:
            mem[temp.val] = mem.get(temp.val, [])
            mem[temp.val].append(temp)
            temp = temp.next
            n += 1
        
        sorted_vals = sorted(mem.keys())

        for i in range(len(sorted_vals)):
            cur_val = sorted_vals[i]
            m = len(mem[cur_val])
            # if length of current numbers is bigger than 1, link them and set last to the next
            if m > 1:
                for j in range(0, m - 1):
                    mem[cur_val][j].next = mem[cur_val][j+1]

            if i == len(sorted_vals) - 1:
                 mem[cur_val][-1].next = None
            else:
                next_val = sorted_vals[i + 1]
                mem[cur_val][-1].next = mem[next_val][0]

        return mem[sorted_vals[0]][0]