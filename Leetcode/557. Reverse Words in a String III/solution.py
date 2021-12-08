class Solution:
    def reverseWords(self, s: str) -> str:
        splitted_words = s.split()
        words_reversed = []

        for word in splitted_words:
            words_reversed.append(word[::-1])

        return " ".join(words_reversed)
