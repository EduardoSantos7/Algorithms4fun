class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        averages = [(nums[i] + nums[n-i-1]) / 2 for i in range(0, n // 2)]
        return min(averages)