class Solution:
    def pivotInteger(self, n: int) -> int:
        _sum = (n*(n+1)) // 2
        m = floor(sqrt(_sum))
        if m*m == _sum:
            return int(m)
        return -1
