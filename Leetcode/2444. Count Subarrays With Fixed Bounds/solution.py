class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Use two pointer to create a dynamic window, two variables for current min and max and a counter of subarrays
        left_bound, subarrays, min_position, max_position = -1, 0, -1, -1
        # Add elements in the window if the current max and min are not over the limits
        for i, right in enumerate(nums):
            if right < minK or right > maxK:
                left_bound = i
            
            if right == minK:
                min_position = i
            if right == maxK:
                max_position = i

            # The number of valid subarrays equals the number of elements between left_bound and 
            # the smaller of the two most recent positions.
            subarrays += max(0, min(min_position, max_position) - left_bound)
        
        return subarrays