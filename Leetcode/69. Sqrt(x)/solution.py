class Solution:
    def mySqrt(self, x: int) -> int:
        inf = 0
        sup = x
        curr = x // 2

        if x == 1:
            return 1

        while curr < x:
            temp = curr * curr

            if temp == x:
                return int(curr)
            if temp > x:
                sup = curr
                curr = (inf + curr) / 2

            else:
                inf = curr
                curr = (sup + curr) / 2

            curr = int(curr)
            if curr == inf:
                return curr

        return int(curr)
