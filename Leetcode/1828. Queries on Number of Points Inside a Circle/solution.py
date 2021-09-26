class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for query in queries:
            count = 0
            x, y, r = query
            for point in points:
                x1, y1 = point
                if (x - x1) ** 2 + (y - y1) ** 2 <= r**2:
                    count += 1

            ans.append(count)

        return ans
