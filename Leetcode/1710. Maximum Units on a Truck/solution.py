class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes_sorted = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        units, i = 0, 0
        while truckSize > 0 and i < len(boxTypes_sorted):
            boxes_used = boxTypes_sorted[i][0] if boxTypes_sorted[i][0] <= truckSize else truckSize
            units += boxTypes_sorted[i][1] * boxes_used
            i += 1
            truckSize -= boxes_used
        
        return units
