class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        group = groups[0]
        n = len(words)
        for i in range(1, n):
            if groups[i] != group:
                res.append(words[i])
                group = groups[i]
        return res
    
        # One liner
        # return [words[0]] + [words[i] for i in range(1, len(words)) if groups[i] != groups[i-1]] 