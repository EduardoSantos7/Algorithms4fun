class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        counter = 0
        for i in range(1, 1001):
            if i not in arr:
                counter += 1
            
            if counter == k:
                return i

        return (k - counter) + 1000