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
            count = 0

            size = len(word)
            mid = size / 2
            while i < mid and word[i].lower() in target_row and word[size - i - 1].lower() in target_row:
                count += 2 if i != (size - i - 1) else 1
                i += 1

            if count == len(word):
                ans.append(word)

        return ans
