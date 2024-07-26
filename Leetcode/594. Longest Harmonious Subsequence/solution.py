class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freqs, _max = Counter(nums), 0
        for freq in freqs:
            if freqs.get(freq+1):
                _max = max(_max, freqs[freq] + freqs[freq+1])
        return _max