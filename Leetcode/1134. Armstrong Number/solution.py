class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum([math.pow(int(d), len(str(n))) for d in str(n)]) == n