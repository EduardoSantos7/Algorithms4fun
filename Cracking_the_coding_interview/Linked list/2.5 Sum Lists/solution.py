def add_lists(l1, l2):
    p1 = p2 = carry = 0
    res = []

    while p1 < len(l1) or p2 < len(l2) or carry:
        val = 0

        if p1 < len(l1):
            val += l1[p1]
            p1 += 1

        if p2 < len(l2):
            val += l2[p2]
            p2 += 1

        if carry:
            val += 1

        digit = val % 10
        carry = 1 if val >= 10 else 0

        res.append(digit)

    return res


# Test

print(add_lists([1, 2, 3], [4, 1, 7]))
