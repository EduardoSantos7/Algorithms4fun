def findThreeLargestNumbers(array):
    result = [None, None, None]
    for elem in array:
        try_to_insert(elem, result)
    return result


def try_to_insert(elem, result):
    if not result[2] or result[2] < elem:
        shift_insert(elem, result, 2)

    elif not result[1] or result[1] < elem:
        shift_insert(elem, result, 1)

    elif not result[0] or result[0] < elem:
        shift_insert(elem, result, 0)


def shift_insert(elem, array, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = elem
        else:
            array[i] = array[i + 1]
