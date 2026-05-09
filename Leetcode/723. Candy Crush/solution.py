class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        changed, board = self._crush_candies(board)

        while changed:
            changed, board = self._crush_candies(board)

        return board

    def _crush_candies(self, board: List[List[int]]) -> (bool, List[List[int]]):
        targets = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    continue

                crushable = self._find_same_number_path(board, i, j)

                for x, y in crushable:
                    targets.add((x, y))

        if not targets:
            return False, board

        board = self._eliminate(board, targets)
        return True, board

    def _find_same_number_path(self, board: List[List[int]], x: int, y: int) -> List[tuple[int, int]]:
        target = board[x][y]
        rows = len(board)
        cols = len(board[0])

        result = []

        # Check horizontal run
        horizontal = [(x, y)]

        j = y - 1
        while j >= 0 and board[x][j] == target:
            horizontal.append((x, j))
            j -= 1

        j = y + 1
        while j < cols and board[x][j] == target:
            horizontal.append((x, j))
            j += 1

        if len(horizontal) >= 3:
            result.extend(horizontal)

        # Check vertical run
        vertical = [(x, y)]

        i = x - 1
        while i >= 0 and board[i][y] == target:
            vertical.append((i, y))
            i -= 1

        i = x + 1
        while i < rows and board[i][y] == target:
            vertical.append((i, y))
            i += 1

        if len(vertical) >= 3:
            result.extend(vertical)

        return result

    def _eliminate(self, board: List[List[int]], targets: set[tuple[int, int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])

        # Crush all targets simultaneously
        for i, j in targets:
            board[i][j] = 0

        # Apply gravity column by column
        for j in range(cols):
            write_row = rows - 1

            # Move non-zero candies down
            for i in range(rows - 1, -1, -1):
                if board[i][j] != 0:
                    board[write_row][j] = board[i][j]
                    write_row -= 1

            # Fill remaining top cells with 0
            for i in range(write_row, -1, -1):
                board[i][j] = 0

        return board