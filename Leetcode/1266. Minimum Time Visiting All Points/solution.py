class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        time = 0
        for i in range(1, len(points)):
            current = points[i]
            last = points[i - 1]
            dif_x = abs(current[0] - last[0])
            dif_y = abs(current[1] - last[1])
            time += max(dif_x, dif_y)
        return time
