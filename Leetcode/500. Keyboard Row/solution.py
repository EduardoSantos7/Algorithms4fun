class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = set(list("qwertyuiop"))
        row_2 = set(list("asdfghjkl"))
        row_3 = set(list("zxcvbnm"))

        ans = []

        for word in words:
            # Detect the row
            target_row = row_1 if word[0].lower() in row_1 else None
            target_row = row_2 if word[0].lower() in row_2 else target_row
            target_row = row_3 if word[0].lower() in row_3 else target_row

            # Check if all the chars are in the same row
            i = 0
            while i < len(word) and word[i].lower() in target_row:
                i += 1

            if i == len(word):
                ans.append(word)

        return ans
