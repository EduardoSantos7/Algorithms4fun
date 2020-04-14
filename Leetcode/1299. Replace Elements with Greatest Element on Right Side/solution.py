class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        for i in range(len(arr) - 1):
            max_n = max(arr[i + 1:])
            arr[i] = max_n
        arr[-1] = -1
        return arr
