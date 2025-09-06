# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = self._get_length(self.head)

    def _get_length(self, head):
        temp = head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        return counter

    def getRandom(self) -> int:
        random_integer = random.randint(0, self.length - 1)
        temp = self.head
        counter = 0

        while temp and counter < random_integer:
            temp = temp.next
            counter += 1

        return temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
