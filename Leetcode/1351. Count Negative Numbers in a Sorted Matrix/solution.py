class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for sub_list in grid:
            for number in sub_list:
                if number < 0:
                    count += 1
        return count
