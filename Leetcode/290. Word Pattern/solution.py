class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mem = {}
        seen = set()

        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            char, w = pattern[i], words[i]

            if not mem.get(char) and w not in seen:
                mem[char] = w
                seen.add(w)
                continue

            if mem.get(char) != w:
                return False

        return True
