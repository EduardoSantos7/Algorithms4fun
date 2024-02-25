class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        frequency_good_pairs = {}

        for i, num in enumerate(nums):
            result = i - num
            if result in frequency_good_pairs:
                good_pairs += frequency_good_pairs[result]
            frequency_good_pairs[result] = frequency_good_pairs[result] + 1 if frequency_good_pairs.get(result) else 1
        
        total_pairs = len(nums) * (len(nums) - 1) // 2
        return total_pairs - good_pairs
