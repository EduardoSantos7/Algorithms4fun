class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_val = -1
        max_idx = 0

        for i in range(n - k + 1):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i

        return nums[max_idx:max_idx + k]
