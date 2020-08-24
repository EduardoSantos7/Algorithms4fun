def palindrome_permutation(string):
    # Ignore the case
    string = string.lower()
    # Replace all non ascii chars
    string = ''.join(
        [i if ord(i) < 128 else '' for i in string]).replace(' ', '')
    odd_numbers = 0
    mem = {}

    for char in string:
        mem[char] = mem.get(char, 0) + 1

        # With thiis we only need 1 pass to check if there's oonly 1 odd number,
        # we can do this in 2 pass but this is something to talk about with the intervewer.
        if mem[char] % 2 == 1:
            odd_numbers += 1
        else:
            odd_numbers -= 1

    return odd_numbers <= 1


# Test
print(palindrome_permutation("Tact Coa"))
