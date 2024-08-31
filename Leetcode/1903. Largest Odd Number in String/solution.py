class Solution:
    def largestOddNumber(self, num: str) -> str:
        if num[-1] in "13579":
            return num
        
        i = len(num) - 1
        while i >= 0 and num[i] not in "13579":
            i -= 1
        
        return num[:i + 1] or ""