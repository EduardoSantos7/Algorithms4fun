class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        res = []
        for i in range(len(s)):
            if s[i] == "6":
                res.append("9")
                res.extend(s[i+1:])
                break
            res.append(s[i])
        return int("".join(res))