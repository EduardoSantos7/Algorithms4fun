class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber, rem = divmod(columnNumber - 1, 26)
            res.append(chr(65+rem))

        return ''.join(reversed(res))
