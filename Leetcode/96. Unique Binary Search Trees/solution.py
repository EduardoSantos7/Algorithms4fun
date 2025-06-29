class Solution:
    def numTrees(self, n: int) -> int:
        answer = 1
        for i in range(0, n):
            answer = answer * 2 * (2 * i + 1) / (i + 2)
        
        return int(answer)
