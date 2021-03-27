class Solution:
    def countPrimes(self, n: int) -> int:
        counter = 0
        mem = [True] * n

        for num in range(2, n):
            if mem[num]:
                counter += 1

                for i in range(num * num, n, num):
                    mem[i] = False

        return counter
