class Solution:
    def greatestLetter(self, s: str) -> str:
        lowercase = set()
        uppercase = set()

        for char in s:
            if char.islower():
                lowercase.add(char)
            else:
                uppercase.add(char)

        for i in reversed(range(ord('A'), ord('Z') + 1)):
            char = chr(i)

            if char in uppercase and char.lower() in lowercase:
                return char

        return ""