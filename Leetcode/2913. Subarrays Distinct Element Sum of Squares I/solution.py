class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mem = set()
        _sum = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                a = i

                while a <= j:
                    mem.add(nums[a])
                    a += 1
                
                _sum += len(mem) * len(mem)
                mem.clear()
        
        return _sum