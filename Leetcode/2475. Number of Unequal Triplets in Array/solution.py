class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        s = list(accumulate(Counter(nums).values()))
        return sum(s[i - 1] * (s[i] - s[i - 1]) * (s[-1] - s[i]) for i in range(1, len(s)))