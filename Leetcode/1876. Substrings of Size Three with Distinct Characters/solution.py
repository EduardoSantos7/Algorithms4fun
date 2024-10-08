class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 2):
            # Could be faster but not scalable if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
            if len(set(s[i : i + 3])) == 3:
                ans += 1
        
        return ans