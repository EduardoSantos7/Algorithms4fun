class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # Check first diagonal
        j = len(grid[0]) - 1
        diagonal_sums = 0
        for i in range(len(grid)):
            if grid[i][i] == 0:
                return False
            if grid[i][j - i] == 0:
                return False
            diagonal_sums += grid[i][i] + grid[i][j - i] if (i, i) != (i, j-i) else grid[i][i]
        
        total_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                total_sum += grid[i][j]
        
        return total_sum == diagonal_sums