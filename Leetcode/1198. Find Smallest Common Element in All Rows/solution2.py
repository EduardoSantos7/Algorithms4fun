class Solution:
    def meta_search(self, row, pos, val):
        sz = len(row)
        d = 1
        while pos < sz and row[pos] < val:
            d <<= 1
            if row[min(pos + d, sz - 1)] >= val:
                d = 1
            pos += d
        return pos

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pos = [0] * n
        cur_max = 0
        cnt = 0

        while True:
            for i in range(n):
                pos[i] = self.meta_search(mat[i], pos[i], cur_max)
                if pos[i] >= m:
                    return -1
                if mat[i][pos[i]] != cur_max:
                    cur_max = mat[i][pos[i]]
                    cnt = 1
                else:
                    cnt += 1
                    if cnt == n:
                        return cur_max