class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric_numbers = 0
        for x in range(low, high + 1):
            num_x = str(x)
            n = len(num_x)

            if n % 2 != 0:
                continue
            
            part_1 = [int(c) for c in num_x[:n//2]]
            part_2 = [int(c) for c in num_x[n//2:]]
            if sum(part_1) == sum(part_2):
                symmetric_numbers += 1
        
        return symmetric_numbers