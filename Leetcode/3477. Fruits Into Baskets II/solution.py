class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)
        allocated = 0

        def can_be_allocated(quantity):
            i = 0
            while i < N:
                if baskets[i] >= quantity:
                    baskets[i] = 0
                    return True
                i += 1

            return False

        for i in range(N):
            allocated += 1 if can_be_allocated(fruits[i]) else 0

        return N - allocated
