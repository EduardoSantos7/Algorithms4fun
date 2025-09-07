class Solution:
    def isThree(self, n: int) -> bool:
        if n == 4:
            return True
        c = 0
        for i in range(3, n//2):
            if n % i == 0:
                c += 1
                if c > 1:
                    return False
        return c == 1