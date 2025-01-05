class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0
        for i in range(len(grid[0])):
            last = grid[0][i]
            for j in range(1, len(grid)):
                if grid[j][i] <= last:
                    last += 1
                    operations += last - grid[j][i]
                else:
                    last = grid[j][i]

        return operations