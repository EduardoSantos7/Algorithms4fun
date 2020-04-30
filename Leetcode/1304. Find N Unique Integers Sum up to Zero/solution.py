class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        loop = n//2 + 1
        rem = n % 2

        if rem == 1:
            res.append(0)
        
        for i in range(1, loop):
            res.append(i)
            res.append(-i)

        return res
