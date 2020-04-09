class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, num in zip(index, nums):
            target.insert(i, num)
        return target
