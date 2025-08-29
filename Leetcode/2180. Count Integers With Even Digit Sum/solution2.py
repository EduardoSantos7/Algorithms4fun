class Solution:
    def countEven(self, num: int) -> int:
        return len([(n, [int(x) for x in list(str(n))]) for n in range(2, num + 1) if sum([int(x) for x in list(str(n))]) % 2 == 0])