class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_zero = 0
        max_ones = 0
        temp = 0

        for i in range(len(s)):
            if i > 0 and i < len(s) and s[i] != s[i-1]:
                temp = 0

            temp += 1

            max_zero = max(temp, max_zero) if s[i] == '0' else max_zero
            max_ones = max(temp, max_ones) if s[i] == '1' else max_ones

        return True if max_ones > max_zero else False
