class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0, 0]
        grid_len = len(grid)
        expected_nums = set([i for i in range(1, grid_len*grid_len + 1)])
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                val = grid[i][j]
                if val in seen:
                    ans[0] = val
                else:
                    expected_nums.remove(val)
                    seen.add(val)

        ans[1] = list(expected_nums)[0]
        return ans