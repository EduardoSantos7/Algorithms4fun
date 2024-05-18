class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        pl, pr = 0, len(s) - 1
        ans = list(s)

        while pl <= pr:
            if s[pl] < s[pr]:
                ans[pl], ans[pr] = s[pl], s[pl]
            else:
                ans[pl], ans[pr] = s[pr], s[pr]
            
            pl += 1
            pr -= 1
        
        return ''.join(ans)
