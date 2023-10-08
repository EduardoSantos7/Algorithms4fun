class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        seen = set()

        for num in nums:
            if (num - diff in seen) and (num - diff - diff in seen):
                ans += 1
            seen.add(num)
        
        return ans