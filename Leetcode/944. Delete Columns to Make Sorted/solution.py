class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        for char in range(len(strs[0])):
            for word in range(1, len(strs)):
                if not strs[word-1][char] <= strs[word][char]:
                    delete += 1
                    break
        return delete
