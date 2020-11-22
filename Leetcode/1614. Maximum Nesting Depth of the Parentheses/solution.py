class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        open_parentheses = 0

        for char in s:
            if char == '(':
                open_parentheses += 1
                max_depth = max(max_depth, open_parentheses)
            elif char == ')':
                open_parentheses -= 1

        return max_depth
