class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # cross multiply the denominators of the slopes and check equality
        slop_1 = (points[1][1] - points[0][1]) * (points[2][0] - points[1][0])
        slop_2 = (points[2][1] - points[1][1]) * (points[1][0] - points[0][0])

        return slop_1 != slop_2