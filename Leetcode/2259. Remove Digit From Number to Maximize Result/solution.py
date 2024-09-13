class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        current_max = 0

        for i in range(len(number)):
            if number[i] == digit:
                current_max = max(current_max, int(f"{number[:i]}{number[i+1:]}"))
        
        return str(current_max)