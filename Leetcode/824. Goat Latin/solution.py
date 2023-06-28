class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        res = []

        def is_vowel(char):
            return char.lower() in "aeiou"

        for i, word in enumerate(words):
            if is_vowel(word[0]):
                res.append(f"{word}ma{'a'*(i+1)}")
                continue

            res.append(f"{word[1:]}{word[0]}ma{'a'*(i+1)}")
    
        return " ".join(res)