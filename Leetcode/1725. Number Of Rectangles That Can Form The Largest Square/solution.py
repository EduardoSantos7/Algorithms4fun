class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        ans = 0
        for rectangle in rectangles:
            rectangleMax = min(rectangle[0], rectangle[1])

            if rectangleMax > maxLen:
                ans = 1
                maxLen = rectangleMax
            elif rectangleMax == maxLen:
                ans += 1
        
        return ans