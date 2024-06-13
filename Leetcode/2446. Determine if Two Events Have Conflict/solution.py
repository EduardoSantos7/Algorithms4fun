class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Convert string to a numeric value
        hours, mins = map(int, event1[0].split(":"))
        start_event1 = hours * 60 + mins
        hours, mins = map(int, event1[1].split(":"))
        end_event1 = hours * 60 + mins
        hours, mins = map(int, event2[0].split(":"))
        start_event2 = hours * 60 + mins
        hours, mins = map(int, event2[1].split(":"))
        end_event2 = hours * 60 + mins
        # Check if there is an intersection between the two time ranges
        if ((start_event1 <= start_event2 and start_event2 <= end_event1) or (start_event1 <= end_event2 and end_event2 <= end_event1)):
            return True
        elif ((start_event2 <= start_event1 and start_event1 <= end_event2) or (start_event2 <= end_event1 and end_event1 <= end_event2)):
            return True
        return False
        