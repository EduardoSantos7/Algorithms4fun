class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        _max = max(freq.values())
        return sum([n for n in freq.values() if n == _max])