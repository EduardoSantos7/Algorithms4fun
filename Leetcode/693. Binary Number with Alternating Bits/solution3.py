class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        return True if "00" not in bin_n and "11" not in bin_n else False