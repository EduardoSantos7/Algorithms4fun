class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count_word1 = Counter(word1)
        count_word2 = Counter(word2)

        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            if abs(count_word1.get(char, 0) - count_word2.get(char, 0)) > 3:
                return False
        
        return True