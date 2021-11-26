class Solution:
    def longestPalindrome(self, s: str) -> int:
        mem = dict()
        two_multiple_count = 0
        solo_count = 0

        for char in s:
            mem[char] = mem.get(char, 0) + 1

        for char in mem:
            integer, module = divmod(mem[char], 2)
            two_multiple_count += integer*2
            solo_count += module

        return two_multiple_count + (1 if solo_count else 0)
