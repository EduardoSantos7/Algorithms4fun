class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq_w1, freq_w2 = Counter(words1), Counter(words2)
        counter = 0
        for k in freq_w1.keys():
            if freq_w1[k] == 1 and freq_w2.get(k, 0) == 1:
                counter += 1
        return counter