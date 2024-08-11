class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        i, j = 0, 1

        while j < len(s):
            if abs(ord(s[i]) - ord(s[j])) == 32:
                s = s[:i] + s[j+1:]
                i, j = 0, 1
                continue
            i += 1
            j += 1
        
        return s