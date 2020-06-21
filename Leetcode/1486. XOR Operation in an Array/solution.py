class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(1, n):
            xor ^= start + 2*i

        return xor
