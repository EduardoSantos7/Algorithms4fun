class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        N = len(arr)
        diff = (arr[-1] - arr[0]) // N
        left, right = 0, N - 1

        while left < right:
            mid = (right + left) // 2
            expected_value = arr[0] + (diff * mid)
            if arr[mid] == expected_value:
                left = mid + 1
            else:
                right = mid

        return arr[0] + diff * left
