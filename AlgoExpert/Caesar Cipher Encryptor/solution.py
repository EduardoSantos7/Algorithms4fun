def caesarCipherEncryptor(string, key):
    shiff = key % 26
    result = []

    for char in string:
        if char.isnumeric():
            result.append(char)
            continue
        if ord(char) + shiff > 122:
            new = 96 + shiff - (122 - ord(char))
        else:
            new = ord(char) + shiff
        result.append(chr(new))
    return ''.join(result)
