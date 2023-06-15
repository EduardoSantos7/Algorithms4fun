class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        j = len(num) - 1

        while num[j] == '0':
            j -= 1

        return num[:j+1]