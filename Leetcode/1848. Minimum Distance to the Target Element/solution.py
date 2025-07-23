class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        possible_targets = [i for i, x in enumerate(nums) if x == target]
        return min([abs(i - start) for i in possible_targets])