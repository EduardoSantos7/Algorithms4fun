import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0

        # Min-heaps for the left and right candidate pools.
        # We store tuples (cost, index) to handle tie-breaking.
        left_heap = []
        right_heap = []

        # Pointers to the next available workers outside the initial candidate pools.
        l, r = 0, len(costs) - 1

        # Phase 1: Initialize the heaps.
        # Populate the left heap.
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, (costs[l], l))
                l += 1

        # Populate the right heap, ensuring no overlap with the left pool.
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(right_heap, (costs[r], r))
                r -= 1

        # Phase 2: Run k hiring sessions.
        for _ in range(k):
            # Get the best candidate from each heap. If a heap is empty,
            # use a placeholder with infinity to ensure the other heap is chosen.
            best_left = left_heap[0] if left_heap else (
                float('inf'), float('inf'))
            best_right = right_heap[0] if right_heap else (
                float('inf'), float('inf'))

            # Compare candidates. Tuple comparison (cost, index) handles the
            # tie-breaking rule automatically.
            if best_left <= best_right:
                cost, _ = heapq.heappop(left_heap)
                total_cost += cost
                # Replenish the left heap with the next worker from the left side.
                if l <= r:
                    heapq.heappush(left_heap, (costs[l], l))
                    l += 1
            else:
                cost, _ = heapq.heappop(right_heap)
                total_cost += cost
                # Replenish the right heap with the next worker from the right side.
                if l <= r:
                    heapq.heappush(right_heap, (costs[r], r))
                    r -= 1

        return total_cost
