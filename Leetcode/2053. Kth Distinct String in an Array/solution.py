class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for word in freq:
            if freq[word] == 1:
                k -= 1
            if k == 0:
                return word
        return ""

# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         freq = Counter(arr)
#         _orderedUniqueStrings = list(filter(lambda x: freq[x] == 1, freq.keys()))
#         return _orderedUniqueStrings[k-1] if k <= len(_orderedUniqueStrings) else ''