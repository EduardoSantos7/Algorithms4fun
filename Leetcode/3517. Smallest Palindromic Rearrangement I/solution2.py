class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # O(1), O(1)
        if len(s) < 4:
            return s

        # O(1), O(1)
        freq = [0] * 26

        # O(N), O(1)
        for char in range(0, len(s) // 2):
            freq[ord(s[char]) % 97] += 1

        # O(1), O(N)
        half_s = "".join([chr(i + 97) * f for i, f in enumerate(freq)])

        # O(N), O(N)
        return (
            f"{half_s}{half_s[::-1]}"
            if len(s) % 2 == 0
            else f"{half_s}{s[len(s) // 2]}{half_s[::-1]}"
        )
