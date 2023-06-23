class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        large = 2*k+1
        ans = [-1] * len(nums)

        if len(nums) < large:
            return ans

        count = sum(nums[: large])

        for i in range(k, len(nums) - k):
            ans[i] = count // large
            # update count
            count -= nums[i-k]
            next_k = i+k+1
            count += nums[next_k] if next_k < len(nums) else 0
        
        return ans
