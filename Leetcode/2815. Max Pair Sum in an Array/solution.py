class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Create a map key = max digit and value is an array of two that contains the biggest two elements
        mem = dict()

        for num in nums:

            biggest_number = self._get_biggest_number(num)

            if biggest_number not in mem:
                mem[biggest_number] = [num]
            elif len(mem[biggest_number]) == 1:
                if num >= mem[biggest_number][0]:
                    mem[biggest_number].append(num)
                else:
                    mem[biggest_number].insert(0, num)
            elif num > mem[biggest_number][1]:
                mem[biggest_number][0] = mem[biggest_number][1]
                mem[biggest_number][1] = num
            elif num > mem[biggest_number][0]:
                mem[biggest_number][0] = num
        _max = -1

        for i in range(9, 0, -1):
            if len(mem.get(i, [])) == 2:
                _max = max(_max, sum(mem[i]))

        return _max

    def _get_biggest_number(self, num: int):
        _max = -1
        while num > 0:
            _max = max(_max, num % 10)
            num //= 10
        return _max