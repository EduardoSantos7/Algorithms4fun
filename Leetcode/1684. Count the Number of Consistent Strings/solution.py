class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0

        for word in words:
            word_set = set(word)
            if len(word_set - allowed_set) == 0:
                count += 1

        return count
