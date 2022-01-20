class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0

        for sentence in sentences:
            len_words = len(sentence.split())
            max_words = max(len_words, max_words)

        return max_words
