class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1, 2, 3]

        if n < 4:
            return mem[n - 1]

        for i in range(n - 3):
            temp = mem[2]
            mem[2] += mem[1]
            mem[1] = temp

        return mem[2]
