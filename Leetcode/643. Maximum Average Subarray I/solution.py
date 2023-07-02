class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        _sum = sum(nums[start:k])
        max_avg = _sum / k
        n = len(nums)

        for i in range(k, n):
            _sum += nums[i]
            _sum -= nums[start]
            start += 1
            avg = _sum/k
            if avg > max_avg:
                max_avg = avg

        return max_avg
