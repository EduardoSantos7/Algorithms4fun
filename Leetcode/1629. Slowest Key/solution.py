class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        current_max = releaseTimes[0]
        slowest_key = keysPressed[0]
        n = len(keysPressed)
        for i in range(1, n):
            t = releaseTimes[i] - releaseTimes[i-1]
            if t > current_max or (t == current_max and keysPressed[i] > slowest_key):
                current_max = t
                slowest_key = keysPressed[i]
        return slowest_key