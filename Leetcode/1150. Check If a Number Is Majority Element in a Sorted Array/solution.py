class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        occurences = 0
        for x in nums:
            if x == target:
                occurences += 1
        return occurences > len(nums) / 2