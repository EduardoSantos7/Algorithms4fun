class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mem = {}
        max_substring_len = 0
        possible_substring = False

        for i, char in enumerate(s):
            if char in mem:
                max_substring_len = max(max_substring_len, i - mem[char] - 1)
                possible_substring = True
            else:
                mem[char] = i

        return max_substring_len if possible_substring else -1
