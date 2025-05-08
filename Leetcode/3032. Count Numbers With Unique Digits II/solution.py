class Solution:
    def numberCount(self, a: int, b: int) -> int:
        return len([n for n in range(a, b + 1) if len(set(str(n))) == len(str(n))])