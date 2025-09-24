class Solution:
    def minimumMoves(self, s: str) -> int:
        i, n, count = 0, len(s), 0

        while i < n:
            if s[i] == "X":
                count += 1
                i += 3
                continue
            i += 1

        return count
