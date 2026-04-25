class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) % 2 == 0:
            new_s = "".join(sorted(s[: len(s) // 2]))
            return f"{new_s}{new_s[::-1]}"

        new_s = "".join(sorted(s[: len(s) // 2]))
        return f"{new_s}{s[(len(s) - 1) // 2]}{new_s[::-1]}"
