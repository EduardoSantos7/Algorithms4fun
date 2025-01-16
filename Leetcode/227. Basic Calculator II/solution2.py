class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
    
        length = len(s)
        current_number = 0
        last_number = 0
        result = 0
        operation = '+'
        
        for i in range(length):
            current_char = s[i]
            
            if current_char.isdigit():
                current_number = current_number * 10 + int(current_char)
            
            # If current_char is an operator (not a digit/whitespace) or we're at the end of the string
            if (not current_char.isdigit() and not current_char.isspace()) or i == length - 1:
                if operation == '+' or operation == '-':
                    result += last_number
                    last_number = current_number if operation == '+' else -current_number
                elif operation == '*':
                    last_number = last_number * current_number
                elif operation == '/':
                    # Use truncation toward zero to match Java integer division behavior
                    last_number = int(last_number / current_number)
                
                operation = current_char
                current_number = 0
        
        result += last_number
        return result