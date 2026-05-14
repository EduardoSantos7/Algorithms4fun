class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        mem = {}

        for i in range(0, len(nums) - 1):
            if nums[i] == key:
                mem[nums[i + 1]] = mem.get(nums[i + 1], 0) + 1
        
        return max(mem,key = mem.get)