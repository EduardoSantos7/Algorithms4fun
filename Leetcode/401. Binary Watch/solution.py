class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        binary_watch = ['0'] * 10
        all_possible_times = []
        self.all_possible_times(binary_watch, turnedOn, 0, all_possible_times, 0)
        return all_possible_times
    
    def all_possible_times(self, binary_watch, turnedOn, current_turned_on, all_possible_times, index):
        if current_turned_on == turnedOn:
            possible_time = self.translate_binary_to_time(binary_watch)
            
            if self.is_valid_time(possible_time):
                all_possible_times.append(possible_time)
            
            return
        
        for i in range(index, 10):
            binary_watch[i] = '1'
            self.all_possible_times(binary_watch, turnedOn, current_turned_on + 1, all_possible_times, i + 1)
            binary_watch[i] = '0'


    def translate_binary_to_time(self, binary_watch: List[str]) -> str:
        hours = int(''.join(binary_watch[0:4]), 2)
        minutes = str(int(''.join(binary_watch[4:]), 2)).zfill(2)
        return f"{hours}:{minutes}"
    
    def is_valid_time(self, time: str) -> bool:
        hours, minutes = time.split(":")
        hours_int, minutes_int = int(hours), int(minutes)

        if len(minutes) != 2:
            return False
        
        if len(hours) == 2 and hours[0] == '0':
            return False
        
        if hours_int > 11:
            return False
        
        if minutes_int > 59:
            return False
        
        return True
