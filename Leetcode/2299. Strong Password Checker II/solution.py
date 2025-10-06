class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        prev = None
        flags = [0,0,0,0]
        for char in password:
            if prev == char:
                return False

            if char.islower():
                flags[0] = 1
            elif char.isupper():
                flags[1] = 1
            elif char.isdigit():
                flags[2] = 1
            elif char in "!@#$%^&*()-+":
                flags[3] = 1

            prev = char
        
        return all(flags)