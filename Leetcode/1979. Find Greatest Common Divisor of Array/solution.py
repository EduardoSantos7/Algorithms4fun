class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # find min and max
        _min = inf
        _max = -inf
        for n in nums:
            _max = max(_max, n)
            _min = min(_min, n)
        
        # Find GCD
        for n in range(_min, 0, -1):
            if _min % n == 0 and _max % n == 0:
                return n