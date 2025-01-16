class Solution:
    def calculate(self, s: str) -> int:
        # Create an stack where the numbers are pushed, same for signs like +, - while * and / are resolved right away 
        # and its result is also stored in the stack
        stack = []
        i = 0
        while i < len(s):
            symbol = s[i]
            # if symbol is a number check if the stack has a number before, in that case combine them if not just push it
            if symbol.isdigit() and stack and isinstance(stack[-1], int):
                num = stack.pop() * 10 + int(symbol)
                stack.append(num)
            elif symbol.isdigit():
                stack.append(int(symbol))
            # if symbol is not a digit then it's a sign, depending its priority act
            elif symbol == "*" or symbol == "/":
                num_1 = stack.pop()
                moves, num_2 = self.get_next_int(s, i)
                i += moves - 1
                result = num_1 * num_2 if symbol == "*" else num_1 // num_2
                stack.append(result)
            elif symbol == "+" or symbol == "-":
                stack.append(symbol)

            i += 1

        # At this point the only operations left are + and - which can be executed in any order
        # or a number in that case that's the final result

        if len(stack) == 1:
            return stack[0]
        
        i = 0
        while i < len(stack):
            if stack[i] == '+':
                result = stack[i-1] + stack[i+1]
                stack[i+1] = result
                i += 1
            elif stack[i] == '-':
                result = stack[i-1] - stack[i+1]
                stack[i+1] = result
                i += 1
            i += 1
        
        return stack[-1]

    def get_next_int(self, s, i):
        stack = []
        counter = 1
        for i in range(i + 1, len(s)):
            if s[i].isdigit():
                stack.append(s[i])
            elif s[i] in "+-*/":
                break

            counter += 1
  
        return counter, int("".join(stack))