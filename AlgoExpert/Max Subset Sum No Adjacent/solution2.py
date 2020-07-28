def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    first, second = max(array[:2]), array[0]

    for index in range(2, len(array)):
        temp = max(array[index] + second, first)
        second = first
        first = temp

    return first
