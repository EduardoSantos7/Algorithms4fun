class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        starting_indexes = [(i, 0) for i in range(len(matrix))] + [(0, j) for j in range(len(matrix[0]))]

        for index in starting_indexes:
            i, j = index[0], index[1]
            element = matrix[i][j]
            i += 1
            j += 1
            while  i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != element:
                    return False
                i += 1
                j += 1
        
        return True
