class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split(" ")
        to_concatenate = [''] * len(splitted)

        for word in splitted:
            to_concatenate[int(word[-1]) - 1] = word[:-1]

        return ' '.join(to_concatenate)
