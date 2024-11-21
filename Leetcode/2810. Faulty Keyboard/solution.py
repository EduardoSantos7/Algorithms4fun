class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for char in s:
            if char != 'i':
                res.append(char)
            else:
                res.reverse()

        return ''.join(res)