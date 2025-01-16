class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        _min = min(nums)
        n = _min + len(nums)
        for i in range(_min, n):
            if i not in nums_set:
                return False
        return True
