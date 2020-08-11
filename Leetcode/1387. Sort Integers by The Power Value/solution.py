class Solution:
    mem = {1: 1}

    def compute(self, n):
        if n == 1 or n in self.mem:
            return self.mem[n]
        if n % 2:
            self.mem[n] = self.compute(n * 3 + 1) + 1
            return self.mem[n]
        else:
            self.mem[n] = self.compute(n / 2) + 1
            return self.mem[n]

    def getKth(self, lo: int, hi: int, k: int) -> int:

        for i in range(lo, hi+1):
            self.compute(i)

        return sorted((self.mem[i], i) for i in range(lo, hi+1))[k - 1][1]
