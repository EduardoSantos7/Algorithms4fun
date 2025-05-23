class Solution:
    def kthCharacter(self, k: int, word = None) -> str:
        word = word or ['a']

        if len(word) >= k:
            return word[k-1]
        
        new_word = []
        for char in word:
            new_word.append("a" if char == 'z' else chr(ord(char) + 1))
        
        return self.kthCharacter(k, word + new_word)