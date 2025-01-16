class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_counter = 0
        # Iterate through the matrix
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Each not seen 1 found increase the counter,
                if grid[i][j] == '1':
                    island_counter += 1
                    # and we perform a dfs/bfs to mark as seen the possible 1s around
                    self.traverse_node(grid, i, j)

        return island_counter

    # Traverse the grid from (i,j) and mark any 1 as seen
    def traverse_node(self, grid, i, j):
        stack = [(i, j)]

        while stack:
            i, j = stack.pop(0)
            node = grid[i][j]
            if node == '1':
                grid[i][j] = '0'
                neighbours = self.get_neighbours(i, j, len(grid), len(grid[0]))
                stack.extend(neighbours)
    
    # Return the valid adjacent coordinates of a point in a grid
    def get_neighbours(self, x, y, n, m):
        neighbours = []
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for nx, ny in moves:
            tx = x + nx
            ty = y + ny

            if tx >= 0 and tx < n and ty >= 0 and ty < m:
                neighbours.append((tx, ty))
        
        return neighbours
