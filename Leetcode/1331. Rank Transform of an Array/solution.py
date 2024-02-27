class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        ranks = { value: index + 1 for index, value in enumerate(sorted_arr) }
        ans = [ranks.get(arr[i]) for i in range(len(arr))]
        
        return ans