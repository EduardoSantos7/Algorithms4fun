class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        stack = list(s[:2])

        for i in range(2, len(s)):
            c = s[i]
            if c == stack[-1] and c == stack[-2]:
                continue
            else:
                stack.append(c)

        return ''.join(stack)
