class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # count the frequency of the characters
        freq = Counter(s)
        # if the unique characters are less than k return 0 else
        distinc = len(freq)
        if distinc < k :
            return 0
        # start removing the characters with the smallest frequency
        to_delete = distinc - k
        sorted_freqs = sorted(freq.values())
        return sum(sorted_freqs[:to_delete])