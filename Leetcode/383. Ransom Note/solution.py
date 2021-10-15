class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False

        return True
