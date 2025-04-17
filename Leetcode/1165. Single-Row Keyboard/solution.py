class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {char: i for i, char in enumerate(keyboard)}
        current_pos = 0
        total = 0
        for char in word:
            total += abs(pos[char] - current_pos)
            current_pos = pos[char]
        
        return total