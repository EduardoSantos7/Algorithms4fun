# Reverse and compare

def reverse_and_compare(items):
    items_reversed = list(reversed(items))

    for i in range(len(items) // 2):
        if items[i] != items_reversed[i]:
            return False

    return True


print(reverse_and_compare([1, 2, 3, 3, 2, 1]))  # True
print(reverse_and_compare([1, 2, 3, 2, 4]))  # False
print(reverse_and_compare([1, 2, 3, 2, 1]))  # True
print(reverse_and_compare([1]))  # True
print(reverse_and_compare([]))  # True
