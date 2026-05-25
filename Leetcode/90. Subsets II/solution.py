class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        temp_array = []
        self.helper(ans, temp_array, 0, nums)
        return ans

    def helper(self, ans, temp_array, current, nums):
        # aaa
        ans.append(list(temp_array))
        for l in range(current, len(nums)):
            # aaa
            if l != current and nums[l] == nums[l - 1]:
                continue
            temp_array.append(nums[l])
            self.helper(ans, temp_array, l + 1, nums)
            temp_array.pop()
