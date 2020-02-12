class Solution:
    def checkRecord(self, s: str) -> bool:
        count_l = 0
        count_a = 0
        prev = ''
        max_l = 0
        for c in s:
            if c == 'A':
                count_a += 1
            elif c == 'L' and prev == 'L':
                count_l += 1
            elif c == 'L':
                count_l = 1
            else:
                count_l = 0
            prev = c
            max_l = max(max_l, count_l)
        return count_a < 2 and max_l < 3
