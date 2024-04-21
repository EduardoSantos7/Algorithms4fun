class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        len_pref = len(pref)
        for word in words:
            if len(word) < len_pref:
                continue
            if word[:len_pref] == pref:
                ans += 1
        return ans