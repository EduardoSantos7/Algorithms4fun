class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for ql, qr in zip(l, r):
            ans.append(self.check(nums, ql, qr))
        return ans
    
    def check(self, nums: List[int], l: int, r: int):
        _max = -inf
        _min = inf
        _set = set()
        for i in range(l, r+1):
            _max = max(_max, nums[i])
            _min = min(_min, nums[i])
            _set.add(nums[i])

        if (_max - _min) % (len(nums[l:r+1]) - 1) != 0:
            return False
        
        diff = (_max - _min) / (len(nums[l:r+1]) - 1)
        
        num = _min + diff
        while num < _max:
            if num not in _set:
                return False
            num += diff
        
        return True