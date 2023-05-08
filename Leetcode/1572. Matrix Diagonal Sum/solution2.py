class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n: int = len(mat)
        mid: int = n // 2
        res: int = 0

        for i in range(mid):
            res += sum([mat[i][i], mat[i][-1-i],
                       mat[-1-i][i], mat[-1-i][-1-i]])

        if n % 2 != 0:
            res += mat[n//2][n//2]

        return res
