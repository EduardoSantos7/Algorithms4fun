from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, str(n)))
        _sum = sum(nums)
        product = reduce((lambda x, y: x*y), nums)

        return product - _sum
