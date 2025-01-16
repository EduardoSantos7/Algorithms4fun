class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # create a matrix of rowSum x colSum filled with zeros
        matrix = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

        # create two pointers to iterate the sum of rows and cols
        col, row = 0, 0

        while row < len(rowSum) and col < len(colSum):
            # Decide how much we can place in matrix[row][col]
            val = min(rowSum[row], colSum[col])
            matrix[row][col] = val

            # Decrement the sums
            rowSum[row] -= val
            colSum[col] -= val

            # Move pointer(s) if a row or column is fully satisfied
            if rowSum[row] == 0:
                row += 1
            if colSum[col] == 0:
                col += 1
        
        return matrix
