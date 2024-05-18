class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        _max = max(nums)
        for i in range(k):
            ans += _max + i
        return ans