class Solution:
    def similarPairs(self, words: List[str]) -> int:
        set_index = dict()
        mem = dict()
        for i, word in enumerate(words):
            # Even this sort approach might seems to be O(nlogn) but it's not
            # because the set of words has a length of max 26.
            word = str(sorted(set(word)))
            if word in set_index:
                set_index[word] += 1
            else:
                set_index[word] = 1
        pairs = 0

        def total_pairs(length: int):
            if length == 1:
                return 0
            if length == 2:
                return 1
            if length in mem:
                return mem[length]
            res = total_pairs(length - 1) + length - 1
            mem[length] = res
            return res

        for indexes in set_index.values():
            # Even this DP approach might seems to be O(n) but it's not
            # because the total_pairs receives the length of the indexes which is max 26
            pairs += total_pairs(indexes)
        
        return pairs