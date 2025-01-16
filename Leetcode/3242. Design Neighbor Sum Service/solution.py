from typing import List

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        # Compute the maximum value to determine the size of the lists
        max_value = max(max(row) for row in grid)
        size = max_value + 1
        self.diagonals = [0] * size
        self.adjacent = [0] * size

        num_rows = len(grid)
        num_cols = len(grid[0]) if num_rows > 0 else 0

        for y in range(num_rows):
            for x in range(num_cols):
                value = grid[y][x]
                self.diagonals[value], self.adjacent[value] = self._analyzeElement(grid, x, y)

    def adjacentSum(self, value: int) -> int:
        return self.adjacent[value]

    def diagonalSum(self, value: int) -> int:
        return self.diagonals[value]

    def _analyzeElement(self, grid: List[List[int]], x: int, y: int) -> (int, int):
        adjacent_sum, diagonal_sum = 0, 0
        num_rows, num_cols = len(grid), len(grid[0])

        # Directions are defined as (dx, dy)
        adjacent_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Sum adjacent cells
        for dx, dy in adjacent_directions:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < num_rows and 0 <= nx < num_cols:
                adjacent_sum += grid[ny][nx]

        # Sum diagonal cells
        for dx, dy in diagonal_directions:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < num_rows and 0 <= nx < num_cols:
                diagonal_sum += grid[ny][nx]

        return diagonal_sum, adjacent_sum
