class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        mem = set()
        res = 0
        for n in nums:
            if n in mem:
                res ^= n
            mem.add(n)
        return res