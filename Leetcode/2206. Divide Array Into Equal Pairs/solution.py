class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mem = {}
        for num in nums:
            mem[num] = mem.get(num) + 1 if mem.get(num) else 1
        
        return all([x % 2 == 0 for x in mem.values()])