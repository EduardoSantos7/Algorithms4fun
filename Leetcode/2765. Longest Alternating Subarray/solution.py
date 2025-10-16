class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        
        positive, count, ans = True, 0, -1
        for i in range(len(nums) - 1):
            j = i + 1
            mover = i
            count = 0
            positive = True
            while j < len(nums):
                if positive and nums[j] == nums[mover] + 1:
                    count += 2 if not count else 1
                    positive = not positive
                elif not positive and nums[j] == nums[mover] - 1:
                    count += 1
                    positive = not positive
                else:
                    break
                mover += 1
                j += 1
                ans = max(ans, count)

        
        return ans