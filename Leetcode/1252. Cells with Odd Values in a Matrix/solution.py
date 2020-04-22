class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # Count the indices frequency in row an columns
        rows = [0] * n
        cols = [0] * m

        for row, col in indices:
            rows[row] ^= 1
            cols[col] ^= 1

        # Count odd numbers
        odds = 0
        for i in range(n):
            for j in range(m):
                if rows[i] ^ cols[j] == 1:
                    odds += 1
        return odds
