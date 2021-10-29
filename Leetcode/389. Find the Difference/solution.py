class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        for char, count in freq_t.items():
            if char not in freq_s or count != freq_s.get(char):
                return char
