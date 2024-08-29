# 1 pass solution
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        diff = [(i, c1) for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2]

        if len(diff) == 2:
            i1, i2 = diff[0][0], diff[1][0]
            return s1[i1] == s2[i2] and s1[i2] == s2[i1]
        
        return False