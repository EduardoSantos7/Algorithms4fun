def productSum(array, level=1):
    total = 0
    for elem in array:
        if type(elem) is int:
            total += elem
        else:
            total += productSum(elem, level=level+1)
    return total * level
