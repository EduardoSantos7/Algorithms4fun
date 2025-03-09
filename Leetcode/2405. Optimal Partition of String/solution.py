class Solution:
    def partitionString(self, s: str) -> int:
        mem = set()
        ans = 0
        for char in s:
            if char not in mem:
                mem.add(char)
            else:
                mem = set(char)
                ans += 1
        return ans + 1