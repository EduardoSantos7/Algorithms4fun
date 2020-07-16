def isMonotonic(array):
    n = len(array)
    if n < 2:
        return True

    trend = None
    for i in range(1, n):
        if array[i] == array[i - 1]:
            continue
        is_increasing = array[i] > array[i - 1]
        if not trend:
            trend = is_increasing
            continue

        if is_increasing != trend:
            return False

    return True
