class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        res, last_consonant = 0, -1
        last_seen_vowels = {v: -1 for v in vowels}

        for i, x in enumerate(word):
            if x not in vowels:
                last_consonant = i
            else:
                last_seen_vowels[x] = i
                res += max(min(last_seen_vowels.values()) - last_consonant, 0)
        
        return res