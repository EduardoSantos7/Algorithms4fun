class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Binary search to find the smallest index where the number of missing numbers >= k
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Missing numbers until arr[mid]
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # The number of missing numbers by index `right` is less than `k`, 
        # so we need to calculate the missing number after arr[right]
        return left + k
