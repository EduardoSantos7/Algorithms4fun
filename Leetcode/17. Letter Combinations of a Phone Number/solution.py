class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        ans = []

        def helper(acum):
            if acum and len(acum) == len(digits):
                ans.append(acum)
                return

            for letter in letters[digits[len(acum)]]:
                helper(acum + letter)

        helper('')
        return ans
