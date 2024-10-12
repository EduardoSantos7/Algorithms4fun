class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = None
        for i, num in enumerate(nums):
            if num == 1:
                if last_one is not None and (i - last_one - 1 < k):
                    return False
                last_one = i
        
        return True