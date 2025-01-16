class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            index = self.get_min_index(nums)
            nums[index] *= multiplier
        
        return nums
    
    def get_min_index(self, _list):
        min_index = 0
        current_min = _list[min_index]

        for index in range(1, len(_list)):
            if _list[index] < current_min:
                current_min = _list[index]
                min_index = index

        return min_index