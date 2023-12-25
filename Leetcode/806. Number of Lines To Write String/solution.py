class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixels = 0
        lines = 1
        for c in s:
            w = widths[ord(c) - 97]
            pixels += w

            if pixels > 100:
                lines += 1
                pixels = w

        return [lines, pixels]