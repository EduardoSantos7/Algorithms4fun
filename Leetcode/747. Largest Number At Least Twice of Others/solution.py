class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        _max = -inf
        m_i = 0
        for i in range(len(nums)):
            if nums[i] > _max:
                _max = nums[i]
                m_i =i

        return m_i if all([n+n <= _max for n in nums if n != _max]) else - 1