class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([w for w in patterns if w in word])