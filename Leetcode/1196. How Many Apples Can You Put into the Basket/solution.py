class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total_weight = sum(weight)
        upper_border = len(weight) - 1
        while total_weight > 5000:
            total_weight -= weight[upper_border]
            upper_border -= 1
        return upper_border + 1