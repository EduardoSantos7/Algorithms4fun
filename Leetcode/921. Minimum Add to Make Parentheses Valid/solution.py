class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for char in S:
            if char == '(':
                stack.append(char)
            elif stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

        return len(stack)
