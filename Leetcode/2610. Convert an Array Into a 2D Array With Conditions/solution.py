class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_freq = {}
        max_freq = 0

        for num in nums:
            existing_freq = nums_freq.get(num)
            nums_freq[num] = existing_freq + 1 if existing_freq else 1
            max_freq = max(max_freq, nums_freq[num])

        # Init list with different memory address. I use [[]] * max_freq, every sublist will have the same address in memory
        matrix = []
        for _ in range(max_freq):
            matrix.append(list())

        for num, freq in nums_freq.items():
            for sublist in matrix[:freq]:
                sublist.append(num)


        return matrix