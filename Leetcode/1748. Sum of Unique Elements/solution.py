class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mem = {}
        for num in nums:
            mem[num] = mem[num] + 1 if num in mem else 1
        return sum([num for num in mem if mem[num] == 1])