class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [''] * len(indices)

        for i in range(len(indices)):
            shuffled[indices[i]] = s[i]

        return ''.join(shuffled)
