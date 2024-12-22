class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(n):
            res = 1
            while n > 0:
                res *= n % 10
                n //= 10
            return res

        while True:
            prod = product(n)
            if prod % t == 0:
                return n
            n += 1