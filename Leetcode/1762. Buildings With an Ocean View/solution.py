class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        with_view = []
        _max = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > _max:
                with_view.append(i)
                _max = heights[i]

        return with_view[::-1]
