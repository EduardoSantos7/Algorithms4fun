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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # Flat the numbers and gets their depht
        queue = nestedList
        queue.append(None)
        depth = 1
        nums = []
        depths = []
        while queue:
            elem = queue.pop(0)
            if elem is None:
                depth += 1
                if len(queue) > 0:
                    queue.append(None)
            elif elem.isInteger():
                nums.append(elem.getInteger())
                depths.append(depth)
            else:
                _list = elem.getList()
                for obj in _list:
                    queue.append(obj)

        max_depth = max(depths)
        ans = 0
        # For each number, get its weight and perform operation
        for num, depth in zip(nums, depths):
            ans += num * ((max_depth - depth) + 1)

        return ans
