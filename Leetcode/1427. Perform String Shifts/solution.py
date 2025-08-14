class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        rotation = sum([amount if direction == 1 else -amount for (direction, amount) in shift])
        rotation = rotation if abs(rotation) < len(s) else rotation % len(s)
        return s[-rotation:] + s[:-rotation]