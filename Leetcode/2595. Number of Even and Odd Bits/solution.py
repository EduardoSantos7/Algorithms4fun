class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bin_num = bin(n)[2:]
        even, odd = 0, 0

        for i, bit in enumerate(bin_num[::-1]):
            if bit != '1':
                continue
            
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return [even, odd]