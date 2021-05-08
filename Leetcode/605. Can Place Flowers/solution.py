class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        count = 0

        for i, flower in enumerate(flowerbed):

            if not flower and (not i or not flowerbed[i-1]) and (i == size-1 or not flowerbed[i+1]):
                count += 1
                flowerbed[i] = 1

            if count >= n:
                return True

        return False
