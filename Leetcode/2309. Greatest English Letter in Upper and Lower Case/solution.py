class Solution:
    def greatestLetter(self, s: str) -> str:
        lowercase = set()
        uppercase = set()

        for char in s:
            if char.islower():
                lowercase.add(char)
            else:
                uppercase.add(char)
        
        uppercase = list(uppercase)
        uppercase.sort(reverse=True)

        for char in uppercase:
            if char.lower() in lowercase:
                return char
        
        return ""