class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur = 60 * int(current[:2]) + int(current[3:])
        target = 60 * int(correct[:2]) + int(correct[3:])
        diff = target - cur
        count = 0
        steps = [60, 15, 5, 1]
        for step in steps:
            count += diff // step
            diff %= step
        return count