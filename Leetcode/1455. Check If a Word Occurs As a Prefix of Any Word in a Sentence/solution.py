class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Use enumerate to get both index and word, and filter to find words starting with searchWord
        return next((index + 1 for index, word in enumerate(sentence.split(" ")) if word.startswith(searchWord)), -1)
