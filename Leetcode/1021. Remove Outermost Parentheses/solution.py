class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        counter = 0
        last = 0
        # Identify the primitives
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                res.append(s[last: i + 1])
                last = i + 1
            
        # Remove the outermost parentheses and Return the new string
        return "".join([s[1:-1] for s in res])