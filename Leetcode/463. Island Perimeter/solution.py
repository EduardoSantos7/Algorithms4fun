class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        # Find the start point
        start_point = ()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    start_point = (i, j)
                    break
            if start_point:
                break

        land = [start_point]
        seen = set(start_point)

        while land:
            plot = land.pop()

            if plot in seen:
                continue

            seen.add(plot)
            adjacent_water = 0
            # Save the position of adjacent land in a stack and
            # Count how many sides are not connected to another land
            if plot[0] - 1 >= 0 and grid[plot[0] - 1][plot[1]]:
                land.append((plot[0] - 1, plot[1]))
            else:
                adjacent_water += 1

            if plot[0] + 1 < len(grid) and grid[plot[0] + 1][plot[1]]:
                land.append((plot[0] + 1, plot[1]))
            else:
                adjacent_water += 1

            if plot[1] - 1 >= 0 and grid[plot[0]][plot[1] - 1]:
                land.append((plot[0], plot[1] - 1))
            else:
                adjacent_water += 1

            if plot[1] + 1 < len(grid[plot[0]]) and grid[plot[0]][plot[1] + 1]:
                land.append((plot[0], plot[1] + 1))
            else:
                adjacent_water += 1

            perimeter += adjacent_water

        return perimeter
