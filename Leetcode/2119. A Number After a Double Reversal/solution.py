class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        str_num = str(num)
        reversed1 = str(int(str_num[::-1]))
        return str_num == reversed1[::-1]