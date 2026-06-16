class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        _sum = 1 * (k if k < numOnes else numOnes)
        k -= numOnes
        if k:
            k -= k if k < numZeros else numZeros
        if k:
            _sum += -1 * (k if k < numNegOnes else numNegOnes)
        return _sum
