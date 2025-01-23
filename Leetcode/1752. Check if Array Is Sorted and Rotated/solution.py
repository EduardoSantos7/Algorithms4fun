class Solution:
    def check(self, nums: List[int]) -> bool:
        def check_valid_start(start, nums):
            position = start + 1
            prev = start
            if position == len(nums):
                    position = 0
            if prev == len(nums):
                prev = 0
            while position != start:
                if nums[position] < nums[prev]:
                    return False
                position += 1
                prev += 1
                if position == len(nums):
                    position = 0
                if prev == len(nums):
                    prev = 0

            return True

        for i in range(len(nums)):
            if check_valid_start(i, nums):
                return True
        return False