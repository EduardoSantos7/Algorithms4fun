class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum([sum([int(digit) for digit in str(num)]) for num in nums]))