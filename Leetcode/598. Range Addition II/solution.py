class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Get a set of operations that will represent the frequency
        # Dequeue every operation and update its frequency and all the smaller ranges
        # Find the biggest frequency and return the product of it

        # Approch 2)
        # Get min x and min y in ops and return its product

        if not ops:
            return m*n
        
        min_x = m
        min_y = n

        # Two pass but nicer
        # min_x = min([x for x,y in ops])
        # min_y = min([y for x,y in ops])

        #One pass
        for op in ops:
            if op[0] < min_x:
                min_x = op[0]
            if op[1] < min_y:
                min_y = op[1]

        return min_x * min_y