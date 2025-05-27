class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        def find(arr, target):
            left, right, mid = 0, len(arr) - 1, 0
            while left <= right:
                mid = (right + left) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return mid
        # Find the index of 0 and N - 1 or closer and do linear search in that range
        start = find(arr, 0)
        end = find(arr, len(arr) - 1)

        for i in range(start, end + 1):
            if arr[i] == i:
                return i
        
        return -1
