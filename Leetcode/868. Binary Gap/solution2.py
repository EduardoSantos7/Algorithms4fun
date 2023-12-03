class Solution:
    def binaryGap(self, n: int) -> int:
        # Transform the integer in its binary representation
        binary_n = bin(n)[2:]
        # Iterate the binary number, if the current position
        # is a 1 start a counter to the next one and compare
        # the length with a global maximum
        longest_distance = 0
        count = 0
        left = 0
        for i, bit in enumerate(binary_n):
            if bit == '1':
                count += 1
                if count == 2:
                    longest_distance = max(longest_distance, i - left)
                    count -= 1
                left = i

        return longest_distance
