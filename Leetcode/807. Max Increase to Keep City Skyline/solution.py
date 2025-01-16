class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        biggest_per_rows = [max(l) for l in grid]
        biggest_per_cols = [max([row[i] for row in grid]) for i in range(len(grid[0]))]
        n = len(grid)
        total_height = 0

        for i in range(n):
            for j in range(n):
                min_max = min(biggest_per_rows[i], biggest_per_cols[j])

                if min_max > grid[i][j]:
                    total_height += min_max - grid[i][j]
        
        return total_height