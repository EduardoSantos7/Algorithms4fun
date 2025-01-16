class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = inf
        index = -1

        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                min_distance = abs(point[0] - x) + abs(point[1] - y)
                if res > min_distance:
                    res = min_distance
                    index = i
        
        return index 