class TimeMap:

    def __init__(self):
        self.timestamp_to_values = [""] * (10**7 + 1)
        self.keys_to_timestamps = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_to_values[timestamp] = value
        self.keys_to_timestamps[key] = [] if  key not in self.keys_to_timestamps else self.keys_to_timestamps[key]
        self.keys_to_timestamps[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys_to_timestamps:
            return ""
        timestamps = self.keys_to_timestamps[key]
        # closest_timestamp = min(timestamps, key=lambda x: abs(x - timestamp))
        closest_timestamp = self.find_closest_sorted(timestamps, timestamp)

        if closest_timestamp > timestamp:
            return ""

        return self.timestamp_to_values[closest_timestamp]

    def find_closest_sorted(self, my_list, target):
        # Ensure the list is sorted
        my_list.sort()
        
        # Find the insertion point for the target number
        i = bisect.bisect_left(my_list, target)
        
        # Check the neighbors to see which is closer
        if i == 0:
            return my_list[0]
        if i == len(my_list):
            return my_list[-1]
        
        before = my_list[i - 1]
        after = my_list[i]
        
        if abs(before - target) <= abs(after - target):
            return before
        else:
            return after
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

