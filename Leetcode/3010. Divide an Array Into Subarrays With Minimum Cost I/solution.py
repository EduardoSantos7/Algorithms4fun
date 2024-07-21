class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1, min2, min3 = nums[0], nums[1], nums[2]

        for i in range(2, len(nums)):
            if min2 > nums[i]:
                min3 = min2
                min2 = nums[i]
            elif min3 > nums[i]:
                min3 = nums[i]
        
        return min1 + min2 + min3