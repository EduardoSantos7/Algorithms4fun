class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mem = {}
        size = len(arr)

        for num in arr:
            mem[num] = mem.get(num, 0) + 1

        for num, reps in mem.items():
            if reps / size > 0.25:
                return num
