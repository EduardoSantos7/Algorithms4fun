class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]

        if len(bin_n) == 1:
            return True

        for i in range(1, len(bin_n)):
            if bin_n[i] != bin_n[i-1]:
                continue
            return False
        
        return True