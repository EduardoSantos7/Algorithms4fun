class Solution:
    def scoreOfString(self, s: str) -> int:
        _sum = 0
        for i in range(0, len(s) - 1):
            _sum += abs(ord(s[i]) - ord(s[i+1]))
        return _sum