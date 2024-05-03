class Solution:
    def pivotInteger(self, n: int) -> int:
        t = n
        while t:
            l_side = t*(1+t)/2
            r_side = (n-t + 1)*(t+n)/2
            if l_side == r_side:
                return t
            t -= 1
        
        return -1