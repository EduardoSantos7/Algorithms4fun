from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def can_capture(i, j, di, dj):
            """Check if the rook can capture in a given direction."""
            while 0 <= i < len(board) - 1 and 0 <= j < len(board[0]) - 1:
                i += di
                j += dj
                
                if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                    return 0  # Out of bounds
                if board[i][j] == "p":
                    return 1
                if board[i][j] != ".":
                    return 0  # Rook's path is blocked by another piece
            return 0

        # Find the Rook's position
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    # Once Rook is found, check all 4 directions for potential captures
                    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                    return sum(can_capture(i, j, di, dj) for di, dj in directions)
