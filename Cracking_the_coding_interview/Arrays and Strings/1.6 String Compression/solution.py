def compress(string):
    com = []

    count = 0
    for i, c in enumerate(string):
        count += 1

        if (i + 1) >= len(string) or string[i + 1] != c:
            com.append(c)
            com.append(str(count))
            count = 0

    return ''.join(com) if len(com) < len(string) else string


# Test
print(compress("aabcccccaaa"))
