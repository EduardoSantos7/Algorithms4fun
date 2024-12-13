class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp_sum = nums[i] + nums[j]
                if temp_sum > max_sum and temp_sum < k:
                    max_sum = temp_sum
        return max_sum or -1