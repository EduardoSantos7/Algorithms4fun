class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_char_ord = ord(word[0])
        all_lower = True
        all_upper = True
        
        for char in word[1:]:
            char_ord = ord(char)
            
            if all_lower and char_ord < 97:
                all_lower = False
            
            if all_upper and char_ord > 90:
                all_upper = False
            
            if not all_lower and not all_upper:
                return False
        
        return all_lower or all_upper if first_char_ord > 64 and first_char_ord < 91 else all_lower
        