class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = {}
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr)):
            count[x] = count.get(x, 0) + 1

            if count[x] == 0:
                nonzero -= 1
            if count[x] == 1:
                nonzero += 1

            count[y] = count.get(y, 0) - 1

            if count[y] == -1:
                nonzero += 1
            if count[y] == 0:
                nonzero -= 1

            if nonzero == 0:
                ans += 1

        return ans
