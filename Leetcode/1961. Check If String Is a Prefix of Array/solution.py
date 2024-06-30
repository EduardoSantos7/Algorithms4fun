class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix_string = ''
        for word in words:
             prefix_string += word
             if prefix_string == s:
                return True
        return False