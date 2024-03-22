class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coordinates = sorted([x for x, _ in points])
        return max([x_coordinates[i + 1] - x_coordinates[i] for i in range(len(x_coordinates) - 1)])