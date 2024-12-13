class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        count = [0] * 1001
        for num in nums:
            count[num] += 1

        lo, hi = 1, 1000

        while lo <= hi:
            if lo + hi >= k or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > (0 if lo < hi else 1):
                    max_sum = max(max_sum, lo + hi)
                lo += 1
        return max_sum