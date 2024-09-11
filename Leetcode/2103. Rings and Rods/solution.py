class Solution:
    def countPoints(self, rings: str) -> int:
        color_counter = {str(k): set() for k in range(10)}

        for i in range(0, len(rings), 2):
            color, position = rings[i], rings[i+1]
            color_counter[position].add(color)
        
        return len([x for x in color_counter if len(color_counter[x]) == 3])