class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        p = 0
        for word in words:
            l = len(word)
            if s[p:p+l] == word:
                p += l
                continue
            elif p == len(s):
                return True
            return False
        return p == len(s)