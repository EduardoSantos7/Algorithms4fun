def findClosestValueInBst(tree, target):
    if not tree:
        return None

    temp = tree
    current_near = temp.value

    while temp:

        if abs(target - temp.value) < abs(target - current_near):
            current_near = temp.value

        if target < temp.value:
            temp = temp.left
        elif target > temp.value:
            temp = temp.right
        else:
            break
    return current_near
