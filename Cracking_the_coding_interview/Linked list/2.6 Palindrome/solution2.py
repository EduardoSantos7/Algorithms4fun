# Iterative approach

def iterate_and_compare(items):
    if len(items) == 1:
        return True
    mid = len(items) // 2
    stack = []

    for i in range(mid):
        stack.append(items[i])

    start = mid if not len(items) % 2 else mid + 1

    for i in range(start, len(items)):
        if items[i] != stack.pop():
            return False

    return True


print(iterate_and_compare([1, 2, 3, 3, 2, 1]))  # True
print(iterate_and_compare([1, 2, 3, 2, 4]))  # False
print(iterate_and_compare([1, 2, 3, 2, 1]))  # True
print(iterate_and_compare([1]))  # True
print(iterate_and_compare([]))  # True
