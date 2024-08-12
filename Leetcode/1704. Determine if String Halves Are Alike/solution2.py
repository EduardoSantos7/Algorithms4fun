class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count(s):
            res = 0
            for c in s:
                if c.upper() in "AEIOU":
                    res += 1
            return res

        return count(s[:len(s)//2]) == count(s[len(s)//2:])