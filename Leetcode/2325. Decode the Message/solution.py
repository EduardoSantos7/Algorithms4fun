class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {" ": " "}
        abc_counter = 97
        for char in key:
            if char not in mapping and char != ' ':
                mapping[char] = chr(abc_counter)
                abc_counter += 1
                continue

        
        decoded = []
        for char in message:
            decoded.append(mapping.get(char, ''))
        
        return ''.join(decoded)