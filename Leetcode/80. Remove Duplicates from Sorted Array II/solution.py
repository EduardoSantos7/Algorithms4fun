class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indexes_to_delete = []
        _map = dict()
        for i, n in enumerate(nums):
            res = _map.get(n, 0)
            if res < 2:
                indexes_to_delete.append(n)
                _map[n] = _map.get(n, 0) + 1

        for i in range(len(indexes_to_delete)):
            nums[i] = indexes_to_delete[i]

        return len(indexes_to_delete)
