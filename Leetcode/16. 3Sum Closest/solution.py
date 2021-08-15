class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums) - 1
        min_dif = float('inf')
        current_sum = None
        res = -1

        for i in range(len(nums) - 2):
            # if the iteration is the same, continue
            if i != 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, n

            while l < r:
                current_sum = nums[i] + nums[r] + nums[l]
                dif = abs(current_sum - target)

                if(dif < min_dif):
                    min_dif = dif
                    res = current_sum

                if current_sum == target:
                    return current_sum
                if current_sum < target:
                    l += 1
                else:
                    r -= 1

        return res
