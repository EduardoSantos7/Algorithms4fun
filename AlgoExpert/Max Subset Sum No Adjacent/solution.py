def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0

    if len(array) < 3:
        return max(array)

    res = len(array) * [0]
    res[0] = array[0]
    res[1] = max(array[0], array[1])

    for index in range(2, len(array)):
        # Keep the biggest sum for each index
        res[index] = max(res[index - 2] + array[index], res[index - 1])

    return res[-1]
