class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        freq = [0] * (N + 1) # The extra spaces will count for all the numbers bigger than N

        for num in nums:
            freq[min(N, num)] += 1
        
        numbers_bigger_equal = 0

        for i in range(N, 0, -1):
            numbers_bigger_equal += freq[i]
            if i == numbers_bigger_equal:
                return i
        
        return -1