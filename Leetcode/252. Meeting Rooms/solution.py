class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # If there's only one interval return True
        if len(intervals) == 1:
            return True
        # Order the intervals by starting time
        intervals.sort(key = lambda x: x[1])
        # From the second interval check if the start is bigger or equal that the previous ending
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        # if it's not return False
        return True