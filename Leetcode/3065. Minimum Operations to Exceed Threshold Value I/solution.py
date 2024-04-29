class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for n in nums:
            if n < k:
                ans += 1
        return ans

# One liner

def minOperations(self, nums: List[int], k: int) -> int:
        return len([n for n in nums if n < k])