class Solution:
    def freqAlphabets(self, s: str) -> str:
        p1 = 0
        p2 = 2
        res = []

        while p1 < len(s):
            if p2 < len(s) and s[p2] == '#':
                res.append(chr(96 + int(s[p1:p2])))
                p1 = p2 + 1
                p2 = p1 + 2
            else:
                res.append(chr(96 + int(s[p1])))

                p1 += 1
                p2 += 1

        return ''.join(res)
