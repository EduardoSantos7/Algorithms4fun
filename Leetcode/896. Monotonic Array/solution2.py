class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        is_increasing = None
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                is_increasing = False
                break
            elif nums[i] < nums[i+1]:
                is_increasing = True
                break
            i += 1

        if is_increasing is None:
            return True

        while i < len(nums) - 1:
            if is_increasing and (nums[i] <= nums[i+1]) is False:
                return False
            if is_increasing is False and (nums[i] >= nums[i+1]) is False:
                return False
            i += 1
        
        return True