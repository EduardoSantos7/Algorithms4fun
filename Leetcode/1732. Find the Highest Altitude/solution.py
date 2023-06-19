class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        altitude = 0

        for i in gain:
            altitude += i
            highest = max(highest, altitude)
        
        return highest
