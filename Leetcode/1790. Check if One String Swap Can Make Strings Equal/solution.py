# 3 pass solution
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if Counter(s1) != Counter(s2):
            return False
        
        diff = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
        
        return diff == 2
