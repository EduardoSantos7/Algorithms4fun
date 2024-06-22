class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end_index = word.find(ch)
        return word[:end_index+1][::-1] + word[end_index+1:] if end_index != -1 else word