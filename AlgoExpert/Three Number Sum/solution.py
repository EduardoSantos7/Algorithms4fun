def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i, num in enumerate(array):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = num + array[left] + array[right]
            if current_sum == targetSum:
                result.append([num, array[left], array[right]])
                right -= 1
                left += 1
            elif current_sum > targetSum:
                right -= 1
            else:
                left += 1
    return result
