class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if len(words) < 2:
            return ''.join(words) + (' ' * spaces)
        balance_spaces = spaces // (len(words) - 1)

        res = []

        for word in words:
            res.append(word)
            if spaces:
                res.append(' ' * (balance_spaces if spaces >
                                  balance_spaces else spaces))
            spaces -= balance_spaces

        if spaces:
            res.append(' ' * spaces)

        return ''.join(res)
