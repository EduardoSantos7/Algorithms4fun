class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start_range = 0  # keep memory of who started the range
        while start_range < len(nums):
            end_range = start_range + 1

            while end_range < len(nums) and nums[end_range] - nums[end_range - 1] == 1:
                end_range += 1

            if start_range != end_range - 1:
                ans.append(f"{nums[start_range]}->{nums[end_range - 1]}")
            else:
                ans.append(f"{nums[start_range]}")

            start_range = end_range

        return ans
