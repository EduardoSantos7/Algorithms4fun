from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> int:
        self.diff[startTime] = self.diff.get(startTime, 0) + 1
        self.diff[endTime] = self.diff.get(endTime, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(cur, res)
        
        return res
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)