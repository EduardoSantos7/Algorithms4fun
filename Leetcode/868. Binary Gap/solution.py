class Solution:
    def binaryGap(self, n: int) -> int:
        # Transform the integer in its binary representation
        binary_n = bin(n)[2:].zfill(8)
        # Iterate the binary number, if the current position
        # is a 1 start a counter to the next one and compare
        # the length with a global maximum
        longest_distance = 0
        current_distance = 0

        for bit in binary_n:
            if bit == '1' and current_distance == 0:
                current_distance += 1
                continue
            if bit == '1' and current_distance != 0:
                longest_distance = max(longest_distance, current_distance)
                current_distance = 1 # reset
                continue
            if current_distance > 0:
                current_distance += 1
        
        return longest_distance