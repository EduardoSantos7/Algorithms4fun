class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum([int(str_num) * (1 if index % 2 == 0 else -1) for index, str_num in enumerate(str(n))])