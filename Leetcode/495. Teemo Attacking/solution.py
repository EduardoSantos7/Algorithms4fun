class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # get time posined for last number (always duration)
        timePoisoned = duration

        # get time posined for previous numbers
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i-1]
            timePoisoned += duration if diff > duration else diff

        return timePoisoned
