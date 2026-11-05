from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:

        m, n = len(rooms), len(rooms[0])
        INF = 2147483647

        # Find all gates
        doors = deque(
            (x, y)
            for x in range(m)
            for y in range(n)
            if rooms[x][y] == 0
        )

        # Find available neighboring rooms
        def next_positions_available(pos_x, pos_y):
            next_positions = []

            if pos_y - 1 >= 0 and rooms[pos_x][pos_y - 1] == INF:
                next_positions.append((pos_x, pos_y - 1))

            if pos_y + 1 < n and rooms[pos_x][pos_y + 1] == INF:
                next_positions.append((pos_x, pos_y + 1))

            if pos_x + 1 < m and rooms[pos_x + 1][pos_y] == INF:
                next_positions.append((pos_x + 1, pos_y))

            if pos_x - 1 >= 0 and rooms[pos_x - 1][pos_y] == INF:
                next_positions.append((pos_x - 1, pos_y))

            return next_positions

        # BFS from all gates simultaneously
        while doors:
            x, y = doors.popleft()

            for next_x, next_y in next_positions_available(x, y):

                # Distance is based on the CURRENT room
                rooms[next_x][next_y] = rooms[x][y] + 1

                # Explore this room later
                doors.append((next_x, next_y))