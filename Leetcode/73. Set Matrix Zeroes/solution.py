class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols, rows = set(), set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        
        for row in rows:
            for i in range(0, len(matrix[0])):
                matrix[row][i] = 0

        for col in cols:
            for i in range(0, len(matrix)):
                matrix[i][col] = 0