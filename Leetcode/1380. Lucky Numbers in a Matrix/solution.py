class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_nums = set()
        res = []

        for row in matrix:
            min_nums.add(min(row))

        for j in range(len(matrix[0])):
            # Get max in the column
            max_col = max([row[j] for row in matrix])
            if max_col in min_nums:
                res.append(max_col)

        return res
