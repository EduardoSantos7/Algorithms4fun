def is_rotation(str1, str2):
    return str2 in (str1 + str1)


# Test
print(is_rotation("waterbottle", "erbottlewat"))
