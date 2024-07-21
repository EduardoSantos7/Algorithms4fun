class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            if num % 3 != 0:
                operations += 1
        return operations