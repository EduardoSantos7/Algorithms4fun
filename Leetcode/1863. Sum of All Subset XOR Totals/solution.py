class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        # Capture each bit that is set in any of the elements
        for num in nums:
            result |= num
        # Multiply by the number of subset XOR totals that will have each bit set
        return result << (len(nums) - 1)