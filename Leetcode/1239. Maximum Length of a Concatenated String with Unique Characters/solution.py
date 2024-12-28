class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.backtracking(arr, 0, Counter())
    
    def backtracking(self, arr: List[str], pos: int, res_map: Counter[str]) -> int:
        # Check for duplicate characters
        if len(res_map) and res_map.most_common(1)[0][1] > 1:
            return 0

        # Recurse through each possible next option
        # and find the best answer
        best = len(res_map)
        for i in range(pos, len(arr)):
            # Check for duplicate characters in word
            # then add the current word to the result map
            # and recurse to the next position
            word_map = Counter(arr[i])
            if len(word_map) != len(arr[i]):
                 continue
            res_map.update(word_map)
            best = max(best, self.backtracking(arr, i + 1, res_map))
            
            # Backtrack the result map before continuing
            for c in word_map:
                if res_map[c] == word_map[c]:
                    del res_map[c]
                else:
                    res_map[c] -= word_map[c]
        return best