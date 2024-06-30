class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mem = set()
        _max = -1

        for num in nums:
            has_counterpart = num * -1 in mem
            mem.add(num)
            if has_counterpart:
                _max = max(_max, abs(num))
        
        return _max