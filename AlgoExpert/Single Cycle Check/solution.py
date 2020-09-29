def hasSingleCycle(array):
    temp = 0
    count = 0

    while count < len(array):
        if count > 0 and temp == 0:
            return False
        count += 1
        temp = get_next_i(temp, array)
    return temp == 0


def get_next_i(current_i, array):
    jump = array[current_i]
    next_i = (current_i + jump) % len(array)
    return next_i if next_i >= 0 else next_i + len(array)
