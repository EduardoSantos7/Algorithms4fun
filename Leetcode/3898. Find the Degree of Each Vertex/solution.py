class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result = [0] * len(matrix)

        for _list in matrix:
            result = [result[i] + _list[i] for i in range(len(_list))]
        
        return result