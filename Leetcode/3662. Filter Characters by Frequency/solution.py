class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        freq = Counter(s)
        ans = []
        for c in s:
            if freq[c] < k:
                ans.append(c)
        return "".join(ans) if ans else ""