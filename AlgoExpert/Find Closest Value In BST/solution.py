def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree)


def findClosestValueInBstHelper(root, target, closest):
    if not root:
        return closest.value
    if abs(target - root.value) < abs(target - closest.value):
        closest = root

    if target < root.value:
        return findClosestValueInBstHelper(root.left, target, closest)
    if target > root.value:
        return findClosestValueInBstHelper(root.right, target, closest)
    return closest.value
