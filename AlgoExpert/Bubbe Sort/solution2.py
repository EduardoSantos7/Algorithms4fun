def bubbleSort(array):
    changes = True
    counter = 0
    while changes:
        changes = False
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                # Swap
                array[i], array[i + 1] = array[i + 1], array[i]
                changes = True
        counter += 1
    return array
