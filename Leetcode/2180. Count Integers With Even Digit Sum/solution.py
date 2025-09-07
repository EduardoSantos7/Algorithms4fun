class Solution:
    def countEven(self, num: int) -> int:
        s = sum(int(d) for d in str(num))
        return num // 2 if s % 2 == 0 else (num - 1) // 2