class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [min(nums[2*i], nums[2*i + 1]) if i % 2 == 0 else max(nums[2*i], nums[2*i + 1]) for i in range(len(nums) // 2)]
        
        return nums[-1]