from typing import List

class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        prefix_end_index = 0

        for i in range(len(sensor1)):
            if sensor1[i] != sensor2[i]:
                prefix_end_index = i
                break
        else:
            # If no mismatch is found, sensors are the same
            return -1

        def shifted_match(a: List[int], b: List[int], start: int) -> bool:
            # Compare a[start:] == b[start+1:]
            for i in range(start, len(a) - 1):
                if a[i] != b[i + 1]:
                    return False
            return True

        sensor1_can_be_shifted = shifted_match(sensor2, sensor1, prefix_end_index)
        sensor2_can_be_shifted = shifted_match(sensor1, sensor2, prefix_end_index)

        if sensor1_can_be_shifted and sensor2_can_be_shifted:
            return -1
        elif sensor1_can_be_shifted:
            return 2
        elif sensor2_can_be_shifted:
            return 1
        else:
            return -1  # Could not determine the bad sensor
