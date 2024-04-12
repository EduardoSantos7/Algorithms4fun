class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            ans.extend([sw for sw in word.split(separator) if sw])
        return ans