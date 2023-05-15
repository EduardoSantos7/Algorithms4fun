class Solution:
    def fib(self, n: int) -> int:
        a,b, c = 0, 1, 1

        if n < 2:
            return n

        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        
        return c