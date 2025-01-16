class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            if word[i] not in "aeiou":
                continue
            
            mem = set()
            j = i
            while j < len(word) and word[j] in "aeiou":
                mem.add(word[j])
                if len(mem) == 5:
                    ans += 1
                j += 1
            
        return ans