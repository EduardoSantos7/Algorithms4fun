class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join([l for l in s if l not in "aeiou"])