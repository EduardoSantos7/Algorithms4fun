class Solution:
    def splitNum(self, num: int) -> int:
        digits = {}
        while num > 0:
            t = num % 10
            num //= 10
            digits[t] = digits.get(t) + 1 if digits.get(t) else 1

        num_1, num_2 = 0, 0
        flag = True
        for i in range(1, 10):
            while digits.get(i):
                if flag:
                    num_1 = num_1 * 10 + i
                else:
                    num_2 = num_2 * 10 + i
                flag = not flag
                digits[i] -= 1
        return num_1 + num_2