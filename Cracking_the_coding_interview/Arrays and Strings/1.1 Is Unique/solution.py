def isUnique(string):
    mem = set()

    for char in string:
        if char not in mem:
            mem.add(char)
        else:
            return False

    return True


print(isUnique("abcc"))
