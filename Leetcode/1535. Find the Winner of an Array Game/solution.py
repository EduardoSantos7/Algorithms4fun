class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)

        p1 = 0
        p2 = 1
        victories = 0

        while victories != k:
            if arr[p1] > arr[p2]:
                victories += 1
                p2 = (p2 + 1) % len(arr)
            else:
                victories = 1
                p1 = p2
                p2 = (p2 + 1) % len(arr)

        return arr[p1]
