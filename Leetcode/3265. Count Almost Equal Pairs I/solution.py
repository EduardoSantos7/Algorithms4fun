class Solution:
    def countPairs(self, nums: List[int]) -> int:
        # for number in nums check if any of the next numbers is almost equal
        pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self._are_almost_equal(nums[i], nums[j]):
                    pairs += 1
        
        return pairs
    
    def _are_almost_equal(self, num1, num2):
        if num1 == num2:
            return True

        # Use the longer number to swap every digit and check if it's the same number as the smaller
        num1_str = str(num1)
        num2_str = str(num2)
        
        if len(num1_str) == len(num2_str) and len(num2_str) == 1:
            return False

        longest_num, shortest_num = (num1_str, num2_str) if len(num1_str) > len(num2_str) else (num2_str, num1_str)
        longest_num = list(longest_num)

        for i in range(len(longest_num)):
            for j in range(i + 1, len(longest_num)):
                longest_num[i], longest_num[j] = longest_num[j], longest_num[i]
                if int(''.join(longest_num)) == int(shortest_num):
                    return True
                # undo
                longest_num[i], longest_num[j] = longest_num[j], longest_num[i]
        
        return False