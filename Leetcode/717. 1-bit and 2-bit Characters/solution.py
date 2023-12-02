class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        res = False
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                res = True
                i += 1
                continue
            
            res = False
            i += 2
        
        return res