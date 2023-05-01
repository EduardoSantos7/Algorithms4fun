class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        set_numbers = set()
        sub_digit_start = None

        for i in range(0, len(word)):
            if word[i].isdigit() and not sub_digit_start:
                sub_digit_start = i
            if sub_digit_start is not None and not word[i].isdigit():
                set_numbers.add(int(word[sub_digit_start:i]))
                sub_digit_start = None

        if sub_digit_start is not None:
            set_numbers.add(int(word[sub_digit_start:]))

        return len(set_numbers)
