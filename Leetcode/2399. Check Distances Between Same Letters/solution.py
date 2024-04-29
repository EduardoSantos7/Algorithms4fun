class Solution:
    def checkDistances(self, s: str, distances: List[int]) -> bool:
        mem = set()
        for char_i in range(len(s)):
            if s[char_i] in mem:
                continue

            distance = distances[(ord(s[char_i]) - 97)]
            other_char_i = char_i + distance + 1
            if other_char_i < len(s) and s[other_char_i] == s[char_i]:
                mem.add(s[char_i])
                continue
            return False
        return True