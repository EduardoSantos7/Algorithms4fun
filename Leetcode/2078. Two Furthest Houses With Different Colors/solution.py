class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        start = 0
        end = n - 1
        ans = 0

        for i in range(n - 1):
            end -= 1
            start += 1

            if colors[0] != colors[start]:
                ans = max(ans, start)
            if colors[-1] != colors[end]:
                ans = max(ans, n - end - 1)
        
        return ans