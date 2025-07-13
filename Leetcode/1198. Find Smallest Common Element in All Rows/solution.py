class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pos = [0] * n
        cur_max = 0
        cnt = 0

        while True:
            for i in range(n):
                while pos[i] < m and mat[i][pos[i]] < cur_max:
                    pos[i] += 1
                if pos[i] >= m:
                    return -1
                if mat[i][pos[i]] != cur_max:
                    cur_max = mat[i][pos[i]]
                    cnt = 1
                else:
                    cnt += 1
                    if cnt == n:
                        return cur_max