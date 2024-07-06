class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        _max = -1
        for row in grid:
            row.sort()
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                _max = max(grid[i][j],_max)
            result += _max
            _max = -1

        return result