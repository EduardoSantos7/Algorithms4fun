class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)
        digits = Counter(str_num)

        _max = -1
        _min = float("inf")

        for digit in digits:
            new_max = int(str_num.replace(digit, '9'))
            _max = max(_max, new_max)
            new_min = int(str_num.replace(digit, '0'))
            _min = min(_min, new_min)

        return _max - _min