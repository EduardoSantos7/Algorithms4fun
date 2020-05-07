class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = [''] * len(s)
        for index, char in enumerate(s):
            if char == '(':
                stack.append((index, char))
            elif char == ')':
                if stack:
                    ind, value = stack.pop()
                    result[ind] = value
                    result[index] = char
            else:
                result[index] = char

        return ''.join(result)
