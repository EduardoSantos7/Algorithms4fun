class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        encoding_str = ""

        def find_all(a_str, sub):
            start = 0
            while True:
                start = a_str.find(sub, start)
                if start == -1: return
                yield start
                start += len(sub) # use start += 1 to find overlapping matches

        for word in sorted(set(words), key=lambda x: len(x), reverse=True):
            indexes = list(find_all(encoding_str, word))

            if not indexes:
                encoding_str += f"{word}#"
                continue
            found = False
            for index in indexes:
                if encoding_str[index + len(word)] == "#":
                    found = True
                    continue
            
            if not found:
                encoding_str += f"{word}#"

        return len(encoding_str)