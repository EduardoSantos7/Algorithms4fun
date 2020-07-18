def longestPeak(array):
    if len(array) < 3:
        return 0
    max_len = 0
    for i in range(1, len(array) - 1):
        left = i - 1
        right = i + 1

        # Check if the current element is a peak
        is_peak = array[left] < array[i] and array[i] > array[right]
        if not is_peak:
            continue

        while left - 1 >= 0 and array[left - 1] < array[left]:
            left -= 1
        while right + 1 < len(array) and array[right] > array[right + 1]:
            right += 1

        max_len = max(max_len, right - left + 1)

    return max_len
