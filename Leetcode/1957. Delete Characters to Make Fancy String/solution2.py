class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        stack = list(s)
        j = 2

        for i in range(2, len(s)):
            c = s[i]
            if c != stack[j-1] or c != stack[j-2]:
                stack[j] = c
                j += 1

        return ''.join(stack[:j])
