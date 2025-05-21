class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.backtracking([], 0, n, k)
        return self.ans

    def backtracking(self, current_array, current_i, n, k):
        if len(current_array) == k:
            self.ans.append(list(current_array))
            return

        for i in range(current_i + 1, n+1):
            current_array.append(i)
            self.backtracking(current_array, i, n, k)
            current_array.pop()
