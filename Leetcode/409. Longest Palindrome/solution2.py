class Solution:
    def longestPalindrome(self, s: str) -> int:
        solo = set()
        two_multiple_count = 0

        for char in s:
            if char in solo:
                two_multiple_count += 1
                solo.remove(char)
            else:
                solo.add(char)

        return two_multiple_count*2 + (1 if solo else 0)
