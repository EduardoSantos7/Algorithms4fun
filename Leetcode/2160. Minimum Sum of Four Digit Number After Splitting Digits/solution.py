class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()
        a=nums[0]+nums[2]
        b=nums[1]+nums[3]
        return int(a) + int(b)