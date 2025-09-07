class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_increasing_list(nums):
            if len(nums) == 1:
                return True
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True

        def reduce_min_sum_pair(nums):
            if len(nums) == 1:
                return nums
            current_min = inf
            min_index = 0
            for i in range(1, len(nums)):
                _sum = nums[i] + nums[i - 1]
                if _sum < current_min:
                    current_min = _sum
                    min_index = i
            nums[min_index - 1] = current_min
            del nums[min_index]
            return nums

        operations = 0
        while not is_increasing_list(nums):
            reduce_min_sum_pair(nums)
            operations += 1

        return operations
