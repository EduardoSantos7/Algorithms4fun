class Solution:
    def averageValue(self, nums: List[int]) -> int:
        _sum = 0
        count = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                _sum += num
                count += 1
        
        return _sum // count if count else 0