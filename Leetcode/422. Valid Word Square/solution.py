class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        return list(map("".join, itertools.zip_longest(*words, fillvalue=""))) == words
