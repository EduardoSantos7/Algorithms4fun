class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        start, end, res = 0, len(nums) - 1, 0

        while start <= end:
            if start == end:
                res += int(str(nums[start]))
            else:
                res += int(str(nums[start]) + str(nums[end]))
            start += 1
            end -= 1
        
        return res