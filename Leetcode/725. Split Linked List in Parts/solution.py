# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # Traverse the list to get the length
        temp = root
        n = 0

        while temp:
            n += 1
            temp = temp.next

        # Generate a tuple with the numbers that represent the len of subgroups
        groups = [n//k] * k
        mod = n % k

        for i in range(0, len(groups)):
            if mod > 0:
                groups[i] += 1
                mod -= 1
            else:
                break

        # Traverse the list to extract the values of the n numbers where n is the subgroup len
        temp_head = root
        answer = []
        for sub_group in groups:
            count = 0
            answer.append(temp_head)
            prev = None
            while temp_head and count < sub_group:
                count += 1
                prev = temp_head
                temp_head = temp_head.next

            if count == sub_group and prev:
                prev.next = None

        return answer
