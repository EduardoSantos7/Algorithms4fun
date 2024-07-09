class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = [0] * len(queries)
        for j in range(len(queries)):
            acum = 0
            query = queries[j]
            for i in range(len(nums)):
                acum += nums[i]
                if acum > query:
                    break
                result[j] = i + 1
        return result
                