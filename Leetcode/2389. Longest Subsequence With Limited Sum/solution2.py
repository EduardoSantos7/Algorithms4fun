class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        accum = list(accumulate(sorted(nums)))
        return [bisect_right(accum, query) for query in queries]
