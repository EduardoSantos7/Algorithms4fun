class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        for chars in zip(*strs):
            if len(set(chars)) != 1:
                return ''.join(prefix)
            prefix.append(chars[0])
        
        return ''.join(prefix)
