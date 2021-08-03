import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = str(math.factorial(n))

        count = 0
        for i in reversed(range(0, len(num))):
            if num[i] == '0':
                count += 1
            else:
                break
        return count
