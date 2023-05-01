class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                cells = 0
                count = 0
                for mi in range(i-1, i+2):
                    for mj in range (j-1, j+2):
                        if mi < 0 or mi >= m:
                            continue
                        if mj < 0 or mj >= n:
                            continue
                        
                        count += img[mi][mj]
                        cells += 1

                result[i][j] = count//cells
        return result