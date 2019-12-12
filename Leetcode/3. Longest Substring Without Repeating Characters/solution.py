class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = dict()
        i = 0
        ans = 0

        for j in range(len(s)):
            if s[j] in mem:
                i = max(mem[s[j]], i)

            ans = max(ans, j - i + 1)
            mem[s[j]] = j + 1

        return ans
