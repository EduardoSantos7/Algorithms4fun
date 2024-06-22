class Solution:
    def sortString(self, s: str) -> str:
        freq = Counter(s)
        res = []
        while any(freq.values()):
            for char in "abcdefghijklmnopqrstuvwxyz":
                if freq.get(char):
                    res.append(char)
                    freq[char] -= 1
            for char in "abcdefghijklmnopqrstuvwxyz"[::-1]:
                if freq.get(char):
                    res.append(char)
                    freq[char] -= 1
        return "".join(res)