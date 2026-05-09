class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])

        while True:
            changed = False

            # 1. Mark horizontal groups
            for i in range(rows):
                for j in range(cols - 2):
                    value = abs(board[i][j])

                    if value == 0:
                        continue

                    if abs(board[i][j + 1]) == value and abs(board[i][j + 2]) == value:
                        board[i][j] = -value
                        board[i][j + 1] = -value
                        board[i][j + 2] = -value
                        changed = True

            # 2. Mark vertical groups
            for i in range(rows - 2):
                for j in range(cols):
                    value = abs(board[i][j])

                    if value == 0:
                        continue

                    if abs(board[i + 1][j]) == value and abs(board[i + 2][j]) == value:
                        board[i][j] = -value
                        board[i + 1][j] = -value
                        board[i + 2][j] = -value
                        changed = True

            # 3. If nothing was marked, board is stable
            if not changed:
                break

            # 4. Gravity
            for j in range(cols):
                write_row = rows - 1

                for i in range(rows - 1, -1, -1):
                    if board[i][j] > 0:
                        board[write_row][j] = board[i][j]
                        write_row -= 1

                for i in range(write_row, -1, -1):
                    board[i][j] = 0

        return board