class Solution:
    def countAsterisks(self, s: str) -> int:
        bar_flag = False
        ans = 0
        for char in s:
            if char == "|":
                bar_flag = not bar_flag
            if char == "*" and not bar_flag:
                ans += 1
        return ans