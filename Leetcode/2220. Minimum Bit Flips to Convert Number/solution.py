class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        goal = f'{goal:b}'
        start = f'{start:b}'
        _max = max(len(goal), len(start))
        goal = goal.zfill(_max)
        start = start.zfill(_max)
        count = 0
        for i in range(_max):
            if start[i] != goal [i]:
                count += 1
        return count