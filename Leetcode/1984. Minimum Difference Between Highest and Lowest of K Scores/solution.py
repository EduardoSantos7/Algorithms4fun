class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[k-1] - nums[0]
        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i-k+1])
        return res