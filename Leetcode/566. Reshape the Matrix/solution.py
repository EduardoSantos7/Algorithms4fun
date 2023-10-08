class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat

        num_rows = len(mat)
        num_cols = len(mat[0])
        
        def find_num(position):
            row = position // num_cols
            col = position % num_cols
            
            return mat[row][col]

        res = [[0]*c for _ in range(r)]
        num = 0
        for i in range(r):
            for j in range(c):
                n = find_num(num)
                num += 1
                res[i][j] = n
    
        return res
