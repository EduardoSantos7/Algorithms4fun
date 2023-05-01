class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
       # Get min x and min y in ops and return its product

        if not ops:
            return m*n
        
        min_x = m
        min_y = n

        seen = set()

        for op in ops:
            if (op[0],op[1]) in seen:
                continue
            seen.add((op[0],op[1]))
            if op[0] < min_x:
                min_x = op[0]
            if op[1] < min_y:
                min_y = op[1]

        return min_x * min_y