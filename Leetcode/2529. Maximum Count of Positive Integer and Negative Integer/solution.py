class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        start_ptr = 0
        end_ptr = len(nums) - 1

        if (nums[start_ptr] > 0 and nums[end_ptr] > 0) or (nums[start_ptr] < 0 and nums[end_ptr] < 0):
            return len(nums)
        zeros = 0
        while start_ptr < len(nums) and nums[start_ptr] <= 0:
            if nums[start_ptr] == 0:
                zeros += 1
            start_ptr += 1
        
        return max(len(nums) - start_ptr , start_ptr - zeros)