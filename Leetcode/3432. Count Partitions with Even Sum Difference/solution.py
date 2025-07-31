class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        current_sum = 0
        ans = 0
        for i in range(0, len(nums) - 1):
            current_sum += nums[i]
            if (current_sum - (total_sum - current_sum)) % 2 == 0:
                ans += 1
        
        return ans