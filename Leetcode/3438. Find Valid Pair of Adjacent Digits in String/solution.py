class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)

        for i in range(0, len(s) - 1):
            a, b = s[i], s[i + 1]

            if a != b and freq[a] == int(a) and freq[b] == int(b):
                return f"{a}{b}"
        
        return ""