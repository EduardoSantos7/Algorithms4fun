class Solution:
    def maxPower(self, s: str) -> int:
        prev = None
        counter = 0
        max_count = 0

        for c in s:
            if c == prev:
                counter += 1
            else:
                prev = c
                counter = 1

            max_count = max(counter, max_count)

        return max_count
