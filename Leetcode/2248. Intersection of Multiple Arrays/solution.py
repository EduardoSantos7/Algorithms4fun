class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for array in nums[1:]:
            res &= set(array)
        
        return sorted(res)
    
# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         return sorted(list(reduce(lambda a, b: set(a) & set(b), nums)))