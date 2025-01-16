class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for ball in range(lowLimit, highLimit + 1):
            value = 0
            while ball > 0:
                value += ball % 10
                ball //= 10

            boxes[value] = 1 if value not in boxes else boxes[value] + 1

        return max(boxes.values()) 