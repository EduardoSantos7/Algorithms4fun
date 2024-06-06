class Solution:
    def isPrefixAndSuffix(self, w1, w2):
        return True if w2.startswith(w1) and w2.endswith(w1) else False 

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1

        return ans