class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        students = 0

        for start, end in zip(startTime, endTime):
            if start <= queryTime and end >= queryTime:
                students += 1

        return students
