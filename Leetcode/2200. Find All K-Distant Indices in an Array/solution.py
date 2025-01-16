class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = set()
        for i in range(len(nums)):
            if nums[i] == key:
                ans.update([j for j in range(i - k, i + k + 1) if j >= 0 and j < len(nums)])
        
        return list(ans)