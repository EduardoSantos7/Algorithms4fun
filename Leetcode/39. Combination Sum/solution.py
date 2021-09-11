class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(solution, start, missing):
            if missing < 0:
                return

            if not missing:
                ans.append(list(solution))
            
            # start from the next number to avoid not unique solutions
            for i in range(start, len(candidates)):
                solution.append(candidates[i])
                backtrack(solution, i, missing - candidates[i])
                solution.pop()
        
        backtrack([], 0, target)
        return ans
