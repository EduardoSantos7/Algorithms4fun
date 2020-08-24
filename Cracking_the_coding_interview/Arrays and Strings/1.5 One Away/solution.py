def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    smallest, longest = (str1, str2) if len(str1) < len(str2) else (str2, str1)
    ptr_s, ptr_l = 0, 0
    count_changes = 0

    while ptr_s < len(smallest) and ptr_l < len(longest):
        if smallest[ptr_s] != longest[ptr_l]:
            if count_changes:
                return False
            else:
                count_changes += 1
                # Should move both pointers but as longest is always moved
                # It's always moved at the end
                if len(str1) == len(str2):
                    ptr_s += 1
        else:
            ptr_s += 1

        ptr_l += 1

    return True


# Test

print(one_away("pale", "ple"))  # true
print(one_away("pales", "pale"))  # true
print(one_away("pale", "bale"))  # true
print(one_away("pale", "bake"))  # false
