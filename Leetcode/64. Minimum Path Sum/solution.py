class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                up = grid[i-1][j] if i-1 >= 0 else inf
                left = grid[i][j-1] if j-1 >= 0 else inf
                if up != inf or left != inf:
                    grid[i][j] += min(up, left)
        return grid[-1][-1]