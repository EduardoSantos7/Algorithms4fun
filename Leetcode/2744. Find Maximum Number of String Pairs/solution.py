class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        mem = set()
        lookup = set(words) # words contain distinc strings, but this helps o(1) look up
        res = 0

        for word in words[:-1]:
            if word in mem:
                continue

            mem.add(word)
            reversed_word = word[::-1]

            if reversed_word != word and reversed_word in lookup:
                res += 1
                mem.add(reversed_word)
        
        return res