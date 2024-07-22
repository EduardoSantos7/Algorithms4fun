class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        seen = set()
        nums.sort()

        while i < j:
            average = (nums[i] + nums[j]) / 2
            if average not in seen:
                seen.add(average)
            i += 1
            j -= 1
        
        return len(seen)
        