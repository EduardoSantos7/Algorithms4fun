class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        scope = 1
        for i in range(1, n+1):
            if i == 2*scope:
                scope = i
            ans[i] = ans[i-scope] + 1
        
        return ans
