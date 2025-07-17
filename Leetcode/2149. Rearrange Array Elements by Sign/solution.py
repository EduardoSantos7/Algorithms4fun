class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1, arr2, result = [], [], []

        for num in nums:
            target_arr = arr1 if num > 0 else arr2
            target_arr.append(num)
        
        for a, b in zip(arr1, arr2):
            result.append(a)
            result.append(b)
        
        return result