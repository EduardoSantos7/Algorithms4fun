class NumArray:
    acum = []

    def __init__(self, nums: List[int]):
        self.acum = [nums[0]]
        for i in range(1, len(nums)):
            self.acum.append(self.acum[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left:
            return self.acum[right] - self.acum[left - 1]
        return self.acum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
