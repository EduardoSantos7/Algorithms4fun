def urlify(string):
    chars = []

    for char in string:
        if char == " ":
            chars.append("%20")
        else:
            chars.append(char)

    return ''.join(chars)


# Test
print(urlify("www.ed sa de.com"))
