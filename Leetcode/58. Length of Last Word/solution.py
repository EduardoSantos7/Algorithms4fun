class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        length = 0
        for c in s:
            if c != ' ':
                counter += 1
            else:
                if counter:
                    length = counter
                counter = 0

        return length if not counter else counter
