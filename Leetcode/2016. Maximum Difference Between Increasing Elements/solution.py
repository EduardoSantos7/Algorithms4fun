class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = 0
        min_ptr, max_ptr = 0, 1

        while max_ptr < len(nums):
            max_diff = max(max_diff, nums[max_ptr] - nums[min_ptr])
            if nums[min_ptr] >= nums[max_ptr]:
                min_ptr = max_ptr
            
            max_ptr += 1

        return max_diff or -1