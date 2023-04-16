class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -inf
        second = -inf
        third = -inf

        for num in nums:
            if first == num or second == num or third == num:
                continue
            
            if first < num:
                third = second
                second = first
                first = num
            elif second < num:
                third = second
                second = num
            elif third < num:
                third = num
            
        return third if third != -inf else first