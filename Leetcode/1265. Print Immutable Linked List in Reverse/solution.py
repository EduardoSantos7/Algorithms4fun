# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        nodes = [head]
        temp = head
        while temp.getNext():
            nodes.append(temp.getNext())
            temp = temp.getNext()

        for i in range(len(nodes) - 1, - 1, -1):
            nodes[i].printValue()