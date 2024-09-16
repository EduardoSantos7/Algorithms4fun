class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        bad_number = False
        last_good = nums[0]

        for i in range(1, len(nums)):
            if not (nums[i] > last_good):
                if bad_number:
                    return False
                
                bad_number = True

                if i == 1 or nums[i] > nums[i - 2]:
                    last_good = nums[i]
                continue

            last_good = nums[i]
        
        return True