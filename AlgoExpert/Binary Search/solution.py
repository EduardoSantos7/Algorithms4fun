def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (right - left) // 2 + left

        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
