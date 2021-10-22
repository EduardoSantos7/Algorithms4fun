class Solution:
    def interpret(self, command: str) -> str:
        current_char = 0
        parsed = []

        while current_char < len(command):
            if command[current_char] == "G":
                parsed.append("G")
            else:
                close_parenthesis = current_char + 1
                while command[close_parenthesis] != ")":
                    close_parenthesis += 1
                parsed.append("o" if close_parenthesis -
                              current_char == 1 else "al")
                current_char = close_parenthesis
            current_char += 1

        return "".join(parsed)
