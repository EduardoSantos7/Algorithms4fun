def check_permutation(str1, str2):
    mem = {}

    if len(str1) != len(str2):
        return False

    for char in str1:
        mem[char] = mem.get(char, 0) + 1

    for char in str2:
        if char not in mem:
            return False

        mem[char] -= 1

        if mem[char] < 0:
            return False

    return True


# Test

print(check_permutation("abc", "cba"))  # True
print(check_permutation("dog", "goD"))  # False
print(check_permutation("dog", "godq"))  # False
