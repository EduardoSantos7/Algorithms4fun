from collections import Counter
from heapq import heapify


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        q = []
        for i in counter:
            q.append((-counter[i], i))
        heapq.heapify(q)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(q)[1])

        return res
