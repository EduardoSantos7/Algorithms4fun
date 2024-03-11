class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        arr = [char for char in s]

        while left <= right:
            if arr[left] == '1':
                left += 1
            
            if arr[right] == '0':
                right -= 1
            
            if left <= right and arr[left] == '0' and arr[right] == '1':
                arr[left] = '1'
                arr[right] = '0'
            
        arr[right] = '0'
        arr[len(s) - 1] = '1'

        return ''.join(arr)