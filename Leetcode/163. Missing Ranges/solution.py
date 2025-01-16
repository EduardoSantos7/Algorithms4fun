class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        ranges = []

        if not nums:
            return [[lower, upper]]
        
        # Range before the start of the nums
        if nums and lower != nums[0]:
            ranges.append([lower, nums[0] - 1])
        # Range missing inside the array
        if n > 1:
            num1, num2 = 0, 1
            
            while num2 < n:
                start = nums[num1] + 1
                end = nums[num2] - 1

                if start != nums[num2]:
                    ranges.append([start, end])
                
                num1 += 1
                num2 += 1

        # Range missing after the last element
        if nums and upper != nums[-1]:
            ranges.append([nums[-1] + 1, upper])
        
        return ranges