class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                expected = grid[i - 1][j] + 1
                operations += 0 if expected <= grid[i][j] else expected - grid[i][j]
                grid[i][j] = grid[i][j] if expected <= grid[i][j] else expected

        return operations