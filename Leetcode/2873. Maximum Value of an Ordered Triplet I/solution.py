class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = 0  # Max value of nums[i] seen so far
        max_ij = 0  # Max value of nums[i] - nums[j] for i < j
        max_triplet_value = 0  # Maximum triplet value

        for num in nums:
            # Calculate the triplet value using the current `num` as `nums[k]`
            max_triplet_value = max(max_triplet_value, max_ij * num)
            
            # Update max_ij: nums[i] - nums[j], using the current `num` as `nums[j]`
            max_ij = max(max_ij, max_i - num)
            
            # Update max_i: the maximum value of nums[i] seen so far
            max_i = max(max_i, num)
        
        return max_triplet_value
