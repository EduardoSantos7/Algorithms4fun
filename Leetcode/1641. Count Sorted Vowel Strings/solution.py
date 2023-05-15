class Solution:
    def countVowelStrings(self, n: int) -> int:
        a, e, i,o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            o += 1
            i += o
            e += i
            a += e
        
        return sum([a,e,i,o,u])
