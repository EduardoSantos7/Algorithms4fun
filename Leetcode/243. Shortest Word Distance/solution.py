class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_word1 = -1
        index_word2 = -1
        min_distance = inf

        for i, word in enumerate(wordsDict):
            if word == word1:
                index_word1 = i
            elif word == word2:
                index_word2 = i
            else:
                continue

            if index_word1 != -1 and index_word2 != -1:
                min_distance = min(min_distance, abs(
                    index_word1 - index_word2))

        return min_distance
