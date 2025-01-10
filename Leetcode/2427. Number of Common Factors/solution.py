class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common_factors = 0
        _min = min(a, b)
        for i in range(1, _min + 1):
            if a % i == 0 and b % i == 0:
                common_factors += 1
        
        return common_factors