import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        root = math.sqrt(area)

        if root % 2 == 0:
            return [int(root), int(root)]

        # Find the number that divided the area
        n = int(root)
        while (area % n) != 0 and n >= 1:
            n -= 1

        return [int(area/n), int(n)]
