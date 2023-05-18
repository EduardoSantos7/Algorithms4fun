class Solution:
    # Bottom-up DP
    def countSquares(self, matrix: List[List[int]]) -> int:
        res: int = 0
        m: int = len(matrix)
        n: int = len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)] # Matrix of zeros of m + 1 and n + 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                    res += dp[i+1][j+1]
        return res
