class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxAscendingSum = nums[0]
        tempSum = nums[0]

        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                tempSum = nums[i]
                continue
            
            tempSum += nums[i]
            maxAscendingSum = max(maxAscendingSum, tempSum)
    
        return maxAscendingSum