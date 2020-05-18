class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len(heights) - sum([a == b for a, b in zip(heights, sorted(heights))])
