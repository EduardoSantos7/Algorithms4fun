class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # create an array of seize of the biggest element in both arrays init in zeros
        _max = max(firstList[-1][1] if firstList else 0, secondList[-1][1] if secondList else 0)
        time = [0 for _ in range(_max + 1)]
        print(time)
        events = firstList + secondList
        # Traverse both list adding 1 in the array per every time slot in the range
        for event in events:
            start, end = event
            for i in range(start, end + 1):
                time[i] += 1
        # for every event check if there where intersections by checking where the sum is bigger than 1
        intersections = []
        print(time)
        for event in firstList:
            start, end = event
            intersection = []
            for i in range(start, end + 1):
                if not intersection and time[i] > 1:
                    intersection.append(i)
                elif intersection and time[i] == 1:
                    intersection.append(i-1)
                    intersections.append(intersection)
                    intersection = []
            if intersection:
                intersection.append(end)
                intersections.append(intersection)

        return intersections
        