class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        answer = 0
        # Create prefix sum array
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i - 1]


        for i, num in enumerate(nums):
            # for each number calculate the start
            start = max(0, i - num)
            # get the sum from the range start..i
            subarray_sum = prefix_sum[i + 1] - prefix_sum[start]
            # add the sum to a global counter
            answer += subarray_sum
        
        return answer