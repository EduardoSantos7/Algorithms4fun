def isMonotonic(array):
    if len(array) < 2:
        return True

    is_non_increasing = True
    is_non_decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_non_decreasing = False
        if array[i] > array[i - 1]:
            is_non_increasing = False

    return is_non_increasing or is_non_decreasing
