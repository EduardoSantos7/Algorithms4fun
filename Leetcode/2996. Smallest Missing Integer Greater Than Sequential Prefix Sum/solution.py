class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        mem = set(nums)
        max_seq_sum = nums[0]

        while i < len(nums) and nums[i] == nums[i-1] + 1:
            max_seq_sum += nums[i]
            i += 1
        
        ans = max_seq_sum
        while True:
            if ans not in mem:
                return ans
            ans += 1