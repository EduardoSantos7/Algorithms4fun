class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller_than_target_count = 0
        target_count = 0
        
        for num in nums:
            if num < target:
                smaller_than_target_count += 1
            if num == target:
                target_count += 1
        
        return [i + smaller_than_target_count for i in range(target_count)]