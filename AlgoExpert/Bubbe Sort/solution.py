def bubbleSort(array):
    changes = True
    while changes:
        changes = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Swap
                array[i], array[i + 1] = array[i + 1], array[i]
                changes = True
    return array
