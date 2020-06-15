def twoNumberSum(array, targetSum):
    mem = {}
    for num in array:
        if mem.get(targetSum - num):
            return [num, targetSum - num]
        mem[num] = mem.get(num, 0) + 1

    return []
