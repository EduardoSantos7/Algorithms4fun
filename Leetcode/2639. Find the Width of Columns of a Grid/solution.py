class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [] * len(grid[0])
        for j in range(len(grid[0])):
            val = 0
            for i in range(len(grid)):
                val = max(val, len(str(grid[i][j])))
            ans.append(val)

        return ans
