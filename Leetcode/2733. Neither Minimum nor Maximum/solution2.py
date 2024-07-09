class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        _min = nums[0]
        _max = nums[0]
        for num in nums:
            _min = min(_min, num)
            _max = max(_max, num)

        for num in nums:
            if num is not _min and num is not _max:
                return num