class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        mem = set()
        n = len(matrix)
        cols = [set() for i in range(n)]

        for row in matrix:
            for i, num in enumerate(row):
                if num > 0 and num <= n + 1:
                    mem.add(num)
                    cols[i].add(num)
            
            if len(mem) != n:
                return False
            
            mem = set()
        
        for mem in cols:
            if len(mem) != n:
                return False
        
        return True