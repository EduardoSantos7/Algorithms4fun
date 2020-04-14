class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        index = 0
        for i in range(len(arr) - 1):
            if i >= index:
                max_n, index = self.max_and_index(arr[i + 1:])
                index += i + 1

            arr[i] = max_n

        arr[-1] = -1
        return arr

    def max_and_index(self, sub_list):
        max_n = max(sub_list)
        index = sub_list.index(max_n)
        return max_n, index
