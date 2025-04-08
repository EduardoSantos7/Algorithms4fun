class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []

        for index in range(len(pattern) + 1):
            stack.append(index + 1)

            if index == len(pattern) or pattern[index] == "I":
                while stack:
                    result.append(str(stack.pop()))

        return "".join(result)
