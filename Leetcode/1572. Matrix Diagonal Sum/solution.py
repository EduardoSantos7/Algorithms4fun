class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n: int = len(mat)
        res: int = 0
        main_diagonal_i: int = 0
        main_diagonal_j: int = 0
        second_diagonal_i: int = 0
        second_diagonal_j: int = n - 1

        for i in range(n):
            res += sum([mat[main_diagonal_i][main_diagonal_j],
                       mat[second_diagonal_i][second_diagonal_j]])
            main_diagonal_i += 1
            main_diagonal_j += 1
            second_diagonal_i += 1
            second_diagonal_j -= 1

        if n % 2 != 0:
            res -= mat[n//2][n//2]

        return res
