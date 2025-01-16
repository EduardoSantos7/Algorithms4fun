class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = -1

        for token in s.split():
            if token.isdigit():
                num = int(token)
                if num <= last:
                    return False
                
                last = num
        
        return True