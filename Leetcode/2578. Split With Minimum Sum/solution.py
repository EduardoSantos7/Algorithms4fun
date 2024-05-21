class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0:
            t = num % 10
            num //= 10
            digits.append(t)
        digits.sort(reverse=True)
        num_1, num_2 = 0, 0
        units = 1
        for i in range(len(digits)):
            if i % 2 == 0:
                num_1 += digits[i]*units
            else:
                num_2 += digits[i]*units
                units *= 10
        return num_1 + num_2