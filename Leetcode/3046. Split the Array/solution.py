class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        frequencies = Counter(nums)
        return not any(
            [val > 2 for val in frequencies.values()])