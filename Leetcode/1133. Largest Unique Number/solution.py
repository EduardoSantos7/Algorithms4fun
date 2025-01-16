class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        counter = Counter(nums)
        _max = max([num for num in counter if counter[num] == 1] or [-1])
        return _max