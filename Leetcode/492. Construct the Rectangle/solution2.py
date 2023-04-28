class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        x0 = 1
        x1 = x0/2+area/(2*x0)
        while(abs(x1-x0) > 1):
            x0 = x1
            x1 = x0/2+area/(2*x0)

        # Find the number that divided the area
        n = int(x1)
        while (area % n) != 0 and n >= 1:
            n -= 1

        return [int(area/n), int(n)]
