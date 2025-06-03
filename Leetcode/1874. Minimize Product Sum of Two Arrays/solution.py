import heapq

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Make a min heap for the num1 and max hip for num2
        min_heap, max_heap = [], []
        for num1, num2 in zip(nums1, nums2):
            heapq.heappush(min_heap, num1)
            heapq.heappush(max_heap, -num2)
        # Pick the min from num1 and max from nums2 till there are no more elements
        product_sum = 0
        for _ in range(len(nums1)):
            product_sum += -heapq.heappop(max_heap) * heapq.heappop(min_heap)
        
        return product_sum