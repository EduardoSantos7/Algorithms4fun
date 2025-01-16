# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        count = 0
        # Put the nested list in a queue with each depth
        queue = [(nested_element, 1) for nested_element in nestedList]
        # while there are elements in the queue
        while queue:
            # Pop the first element from the queue
            element, depth = queue.pop(0)
            # if the element is an integer multiply it by its depth and add that result to a global counter
            if element.isInteger():
                count += depth * element.getInteger()
            # if it's a list append each of the elements in the queue and increase the depth
            else:
                queue.extend([(nested_element, depth + 1) for nested_element in element.getList()])
        # return the global counter
        return count
