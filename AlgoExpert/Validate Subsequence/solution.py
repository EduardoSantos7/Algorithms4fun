def isValidSubsequence(array, sequence):
    cur_target = 0
    for num in array:
        if num == sequence[cur_target]:
            cur_target += 1
            if cur_target == len(sequence):
                return True
    return False
