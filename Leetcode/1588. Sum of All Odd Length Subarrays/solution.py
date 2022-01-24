class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_length_array_sum = 2 * \
            sum(arr) if len(arr) > 1 and len(arr) % 2 else sum(arr)
        odd_length = 3

        for odd_length in range(odd_length, len(arr), 2):
            i = 0
            while len(arr[i: i + odd_length]) == odd_length:
                odd_length_array_sum += sum(arr[i: i + odd_length])
                i += 1

        return odd_length_array_sum
