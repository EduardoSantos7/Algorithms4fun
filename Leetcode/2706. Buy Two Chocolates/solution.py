class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        _sum = prices[0] + prices[1]
        return money - _sum if _sum <= money else money