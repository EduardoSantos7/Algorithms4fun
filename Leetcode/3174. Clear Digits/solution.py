class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i].isdigit():
                res.pop()
            else:
                res.append(s[i])
        return ''.join(res)
