class Solution:
    def oddString(self, words: List[str]) -> str:
        mem_vals = dict()
        def get_difference(word: str):
            res = []
            for i in range(len(word) - 1):
                if not mem_vals.get(word[i+1]):
                    mem_vals[word[i+1]] = ord(word[i+1]) - ord('a')
                if not mem_vals.get(word[i]):
                    mem_vals[word[i]] = ord(word[i]) - ord('a')
                next_char = mem_vals[word[i+1]]
                current_char = mem_vals[word[i]]
                res.append(next_char - current_char)
            return res
        def all_same(items):
            return all(x == items[0] for x in items)
        differences = [get_difference(words[0]), get_difference(words[1]), get_difference(words[2])]
        if all_same(differences):
            pattern = differences[0]
            for word in words[3:]:
                if get_difference(word) != pattern:
                    return word
        else:
            if differences[0] == differences[1]:
                return words[2]
            elif differences[2] == differences[1]:
                return words[0]
            else:
                return words[1]