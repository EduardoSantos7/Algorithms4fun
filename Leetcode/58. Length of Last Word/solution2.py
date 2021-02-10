class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')

        while words:
            last_word = words.pop()

            if last_word:
                return len(last_word)
        return 0
